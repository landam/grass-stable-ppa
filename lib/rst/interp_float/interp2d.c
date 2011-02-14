
/*-
 *
 * Original program and various modifications:
 * Lubos Mitas 
 *
 * GRASS4.1 version of the program and GRASS4.2 modifications:
 * H. Mitasova,
 * I. Kosinovsky, D. Gerdes
 * D. McCauley 
 *
 * Copyright 1993, 1995:
 * L. Mitas ,
 * H. Mitasova,
 * I. Kosinovsky,
 * D.Gerdes 
 * D. McCauley
 *
 * modified by McCauley in August 1995
 * modified by Mitasova in August 1995, Nov. 1996
 * bug fixes(mask) and modif. for variable smoothing Mitasova Jan 1997
 *
 */


#include <stdio.h>
#include <math.h>
#include <unistd.h>
#include <grass/gis.h>
#include <grass/bitmap.h>

#include <grass/interpf.h>


#define CEULER .57721566


int IL_grid_calc_2d(struct interp_params *params, struct quaddata *data,	/* given segment */
		    struct BM *bitmask,	/* bitmask */
		    double zmin, double zmax,	/* min and max input z-values */
		    double *zminac, double *zmaxac,	/* min and max interp. z-values */
		    double *gmin, double *gmax,	/* min and max inperp. slope val. */
		    double *c1min, double *c1max, double *c2min, double *c2max,	/* min and max interp. curv. val. */
		    double *ertot,	/* total interplating func. error */
		    double *b,	/* solutions of linear equations */
		    int offset1,	/* offset for temp file writing */
		    double dnorm)

/*
 * Calculates grid for the given segment represented by data (contains
 * n_rows, n_cols, ew_res,ns_res, and all points inside + overlap) using
 * solutions of system of lin. equations and interpolating functions
 * interp() and interpder(). Also calls secpar() to compute slope, aspect
 * and curvatures if required.
 */
{

    /*
     * C C       INTERPOLATION BY FUNCTIONAL METHOD : TPS + complete regul.
     * c
     */
    double x_or = data->x_orig;
    double y_or = data->y_orig;
    int n_rows = data->n_rows;
    int n_cols = data->n_cols;
    int n_points = data->n_points;
    struct triple *points;
    static double *w2 = NULL;
    static double *w = NULL;
    int cond1, cond2;
    double r;
    double stepix, stepiy, xx, xg, yg, xx2;
    double rfsta2, /* cons, cons1, */ wm, dx, dy, dxx, dyy, dxy, h, bmgd1,
	bmgd2;
    double r2, gd1, gd2;	/* for interpder() */
    int n1, k, l, m;
    int ngstc, nszc, ngstr, nszr;
    double zz;
    int bmask = 1;
    static int first_time_z = 1;
    int offset, offset2;
    double fstar2 = params->fi * params->fi / 4.;
    double tfsta2, tfstad;
    double ns_res, ew_res;
    double rsin = 0, rcos = 0, teta, scale = 0;	/*anisotropy parameters - added by JH 2002 */
    double xxr, yyr;

    if (params->theta) {
	teta = params->theta / 57.295779;	/* deg to rad */
	rsin = sin(teta);
	rcos = cos(teta);
    }
    if (params->scalex)
	scale = params->scalex;

    ns_res = (((struct quaddata *)(data))->ymax -
	      ((struct quaddata *)(data))->y_orig) / data->n_rows;
    ew_res = (((struct quaddata *)(data))->xmax -
	      ((struct quaddata *)(data))->x_orig) / data->n_cols;

    /*  tfsta2 = fstar2 * 2.; modified after removing normalization of z */
    tfsta2 = (fstar2 * 2.) / dnorm;
    tfstad = tfsta2 / dnorm;
    points = data->points;

    /*
     * normalization
     */
    stepix = ew_res / dnorm;
    stepiy = ns_res / dnorm;

    cond2 = ((params->adxx != NULL) || (params->adyy != NULL) ||
	     (params->adxy != NULL));
    cond1 = ((params->adx != NULL) || (params->ady != NULL) || cond2);

    if (!w) {
	if (!(w = (double *)G_malloc(sizeof(double) * (params->KMAX2 + 9)))) {
	    fprintf(stderr, "Cannot allocate w\n");
	    return -1;
	}
    }
    if (!w2) {
	if (!(w2 = (double *)G_malloc(sizeof(double) * (params->KMAX2 + 9)))) {
	    fprintf(stderr, "Cannot allocate w2\n");
	    return -1;
	}
    }
    n1 = n_points + 1;
    /*
     * C C         INTERPOLATION   *  MOST INNER LOOPS ! C
     */
    ngstc = (int)(x_or / ew_res + 0.5) + 1;
    nszc = ngstc + n_cols - 1;
    ngstr = (int)(y_or / ns_res + 0.5) + 1;
    nszr = ngstr + n_rows - 1;


    for (k = ngstr; k <= nszr; k++) {
	offset = offset1 * (k - 1);	/* rows offset */
	yg = (k - ngstr) * stepiy + stepiy / 2.;	/* fixed by J.H. in July 01 */
	for (m = 1; m <= n_points; m++) {
	    wm = yg - points[m - 1].y;
	    w[m] = wm;
	    w2[m] = wm * wm;
	}
	for (l = ngstc; l <= nszc; l++) {
	    if (bitmask != NULL)
		/*      if(params->maskmap != NULL)  PK Apr 03 MASK support */
		bmask = BM_get(bitmask, l - 1, k - 1);	/*fixed by helena jan 97 */
	    /*    if(bmask==0 || bmask==-1) fprintf(stderr, "bmask=%d, at (%d,%d)\n", bmask, l, k); */
	    xg = (l - ngstc) * stepix + stepix / 2.;	/*fixed by J.H. in July 01 */
	    dx = 0.;
	    dy = 0.;
	    dxx = 0.;
	    dyy = 0.;
	    dxy = 0.;
	    zz = 0.;
	    if (bmask == 1) {	/* compute everything for area which is
				 * not masked out */
		h = b[0];
		for (m = 1; m <= n_points; m++) {
		    xx = xg - points[m - 1].x;
		    if ((params->theta) && (params->scalex)) {
			/* we run anisotropy */
			xxr = xx * rcos + w[m] * rsin;
			yyr = w[m] * rcos - xx * rsin;
			xx2 = xxr * xxr;
			w2[m] = yyr * yyr;
			r2 = scale * xx2 + w2[m];
			r = r2;
			rfsta2 = scale * xx2 + w2[m];
		    }
		    else {
			xx2 = xx * xx;
			r2 = xx2 + w2[m];
			r = r2;
			rfsta2 = xx2 + w2[m];
		    }

		    h = h + b[m] * params->interp(r, params->fi);
		    if (cond1) {
			if (!params->interpder(r, params->fi, &gd1, &gd2))
			    return -1;
			bmgd1 = b[m] * gd1;
			dx = dx + bmgd1 * xx;
			dy = dy + bmgd1 * w[m];
			if (cond2) {
			    bmgd2 = b[m] * gd2;
			    dxx = dxx + bmgd2 * xx2 + bmgd1;
			    dyy = dyy + bmgd2 * w2[m] + bmgd1;
			    dxy = dxy + bmgd2 * xx * w[m];
			}
		    }
		}

		/*      zz = (h * dnorm) + zmin; replaced by helena jan. 97 due to removing norma
		   lization of z and zm in segmen2d.c */
		zz = h + zmin;
		if (first_time_z) {
		    first_time_z = 0;
		    *zmaxac = *zminac = zz;
		}
		*zmaxac = amax1(zz, *zmaxac);
		*zminac = amin1(zz, *zminac);
		if ((zz > zmax + 0.1 * (zmax - zmin))
		    || (zz < zmin - 0.1 * (zmax - zmin))) {
		    static int once = 0;

		    if (!once) {
			once = 1;
			fprintf(stderr, "WARNING:\n");
			fprintf(stderr,
				"Overshoot -- increase in tension suggested.\n");
			fprintf(stderr, "Overshoot occures at (%d,%d) cell\n",
				l, k);
			fprintf(stderr,
				"The z-value is %f,zmin is %f,zmax is %f\n",
				zz, zmin, zmax);
		    }
		}


		params->az[l] = (FCELL) zz;
		/*
		 * fprintf(stderr,"%f ",zz);
		 */
		if (cond1) {
		    params->adx[l] = (FCELL) (-dx * tfsta2);
		    params->ady[l] = (FCELL) (-dy * tfsta2);
		    if (cond2) {
			params->adxx[l] = (FCELL) (-dxx * tfstad);
			params->adyy[l] = (FCELL) (-dyy * tfstad);
			params->adxy[l] = (FCELL) (-dxy * tfstad);
		    }
		}

	    }
	    else {
		G_set_d_null_value(params->az + l, 1);
		/*          fprintf (stderr, "zz=%f, az[l]=%f, c=%d\n", zz, params->az[l], l); */

		if (cond1) {
		    G_set_d_null_value(params->adx + l, 1);
		    G_set_d_null_value(params->ady + l, 1);
		    if (cond2) {
			G_set_d_null_value(params->adxx + l, 1);
			G_set_d_null_value(params->adyy + l, 1);
			G_set_d_null_value(params->adxy + l, 1);
		    }
		}
	    }

	}
	if (cond1 && (params->deriv != 1)) {
	    if (params->secpar(params, ngstc, nszc, k, bitmask,
			       gmin, gmax, c1min, c1max, c2min, c2max, cond1,
			       cond2) < 0)
		return -1;
	}

	offset2 = (offset + ngstc - 1) * sizeof(FCELL);
	if (params->wr_temp(params, ngstc, nszc, offset2) < 0)
	    return -1;
    }
    return 1;
}
