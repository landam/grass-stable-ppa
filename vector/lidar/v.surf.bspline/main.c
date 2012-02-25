
/**********************************************************************
 *
 * MODULE:       v.surf.bspline
 *
 * AUTHOR(S):    Roberto Antolin & Gonzalo Moreno
 *
 * PURPOSE:      Spline Interpolation
 *
 * COPYRIGHT:    (C) 2006 by Politecnico di Milano -
 *			     Polo Regionale di Como
 *
 *               This program is free software under the
 *               GNU General Public License (>=v2).
 *               Read the file COPYING that comes with GRASS
 *               for details.
 *
 **********************************************************************/

/* INCLUDES */
#include <stdlib.h>
#include <string.h>
#include <math.h>
#include <grass/gis.h>
#include <grass/Vect.h>
#include <grass/dbmi.h>
#include <grass/glocale.h>
#include <grass/config.h>
#include <grass/PolimiFunct.h>
#include "bspline.h"

/* GLOBAL VARIABLES */
int bspline_field;
char *bspline_column;

/*--------------------------------------------------------------------*/
int main(int argc, char *argv[])
{
    /* Variable declarations */
    int nsply, nsplx, nrows, ncols, nsplx_adj, nsply_adj;
    int nsubregion_col, nsubregion_row, subregion_row, subregion_col;
    int subregion = 0, nsubregions = 0;
    int last_row, last_column, grid, bilin, ext, flag_auxiliar, cross;	/* booleans */
    double passoN, passoE, lambda, mean;
    double N_extension, E_extension, orloE, orloN;

    const char *mapset, *dvr, *db, *vector, *map;
    char table_name[GNAME_MAX], title[64];
    char xname[GNAME_MAX], xmapset[GMAPSET_MAX];

    int dim_vect, nparameters, BW;
    int *lineVect;		/* Vector restoring primitive's ID */
    double **raster_matrix;	/* Matrix to store the auxiliar raster values */
    double *TN, *Q, *parVect;	/* Interpolating and least-square vectors */
    double **N, **obsVect;	/* Interpolation and least-square matrix */

    /* Structs declarations */
    int raster;
    struct Map_info In, In_ext, Out;
    struct History history;

    struct GModule *module;
    struct Option *in_opt, *in_ext_opt, *out_opt, *out_map_opt, *passoE_opt,
	*passoN_opt, *lambda_f_opt, *type_opt, *dfield_opt, *col_opt;
    struct Flag *cross_corr_flag, *spline_step_flag;

    struct Reg_dimens dims;
    struct Cell_head elaboration_reg, original_reg;
    BOUND_BOX general_box, overlap_box;

    struct Point *observ;
    struct line_pnts *points;
    struct line_cats *Cats;
    dbCatValArray cvarr;

    int nrec, ctype = 0;
    struct field_info *Fi;
    dbDriver *driver, *driver_cats;

    /*----------------------------------------------------------------*/
    /* Options declarations */
    module = G_define_module();
    module->keywords = _("vector, interpolation");
    module->description =
	_("Bicubic or bilinear spline interpolation with Tykhonov regularization.");

    cross_corr_flag = G_define_flag();
    cross_corr_flag->key = 'c';
    cross_corr_flag->description =
	_("Find the best Tykhonov regularizing parameter using a \"leave-one-out\" cross validation method");

    spline_step_flag = G_define_flag();
    spline_step_flag->key = 'e';
    spline_step_flag->label = _("Estimate point density and distance");
    spline_step_flag->description =
	_("Estimate point density and distance for the input vector points within the current region extends and quit");

    in_opt = G_define_standard_option(G_OPT_V_INPUT);

    in_ext_opt = G_define_standard_option(G_OPT_V_INPUT);
    in_ext_opt->key = "sparse";
    in_ext_opt->required = NO;
    in_ext_opt->description =
	_("Name of input vector map of sparse points");

    out_opt = G_define_standard_option(G_OPT_V_OUTPUT);
    out_opt->required = NO;

    out_map_opt = G_define_standard_option(G_OPT_R_OUTPUT);
    out_map_opt->key = "raster";
    out_map_opt->required = NO;

    passoE_opt = G_define_option();
    passoE_opt->key = "sie";
    passoE_opt->type = TYPE_DOUBLE;
    passoE_opt->required = NO;
    passoE_opt->answer = "4";
    passoE_opt->description =
	_("Length of each spline step in the east-west direction");
    passoE_opt->guisection = _("Settings");

    passoN_opt = G_define_option();
    passoN_opt->key = "sin";
    passoN_opt->type = TYPE_DOUBLE;
    passoN_opt->required = NO;
    passoN_opt->answer = "4";
    passoN_opt->description =
	_("Length of each spline step in the north-south direction");
    passoN_opt->guisection = _("Settings");

    type_opt = G_define_option();
    type_opt->key = "method";
    type_opt->type = TYPE_STRING;
    type_opt->required = NO;
    type_opt->description = _("Spline interpolation algorithm");
    type_opt->options = "bilinear,bicubic";
    type_opt->answer = "bilinear";
    type_opt->guisection = _("Settings");

    lambda_f_opt = G_define_option();
    lambda_f_opt->key = "lambda_i";
    lambda_f_opt->type = TYPE_DOUBLE;
    lambda_f_opt->required = NO;
    lambda_f_opt->description = _("Tykhonov regularization parameter (affects smoothing)");
    lambda_f_opt->answer = "0.01";
    lambda_f_opt->guisection = _("Settings");

    dfield_opt = G_define_standard_option(G_OPT_V_FIELD);
    dfield_opt->description =
	_("If set to 0, z coordinates are used. (3D vector only)");
    dfield_opt->answer = "0";
    dfield_opt->gisprompt = "old_layer,layer,layer_zero";
    dfield_opt->guisection = _("Settings");

    col_opt = G_define_standard_option(G_OPT_COLUMN);
    col_opt->key = "column";
    col_opt->required = NO;
    col_opt->description =
	_("Attribute table column with values to interpolate (if layer>0)");
    col_opt->guisection = _("Settings");

    /*----------------------------------------------------------------*/
    /* Parsing */
    G_gisinit(argv[0]);
    if (G_parser(argc, argv))
	exit(EXIT_FAILURE);

    vector = out_opt->answer;
    map = out_map_opt->answer;

    if (vector && map)
	G_fatal_error(_("Choose either vector or raster output, not both"));

    if (!vector && !map && !cross_corr_flag->answer)
	G_fatal_error(_("No raster or vector or cross-validation output"));

    if (!strcmp(type_opt->answer, "bilinear"))
	bilin = P_BILINEAR;
    else
	bilin = P_BICUBIC;

    passoN = atof(passoN_opt->answer);
    passoE = atof(passoE_opt->answer);
    lambda = atof(lambda_f_opt->answer);
    bspline_field = atoi(dfield_opt->answer);
    bspline_column = col_opt->answer;
    
    flag_auxiliar = FALSE;

    if (!(db = G__getenv2("DB_DATABASE", G_VAR_MAPSET)))
	G_fatal_error(_("Unable to read name of database"));

    if (!(dvr = G__getenv2("DB_DRIVER", G_VAR_MAPSET)))
	G_fatal_error(_("Unable to read name of driver"));

    /* Setting auxiliar table's name */
    if (vector) {
	if (G__name_is_fully_qualified(out_opt->answer, xname, xmapset)) {
	    sprintf(table_name, "%s_aux", xname);
	}
	else
	    sprintf(table_name, "%s_aux", out_opt->answer);
    }

    /* Something went wrong in a previous v.surf.bspline execution */
    if (db_table_exists(dvr, db, table_name)) {
	/* Start driver and open db */
	driver = db_start_driver_open_database(dvr, db);
	if (driver == NULL)
	    G_fatal_error(_("No database connection for driver <%s> is defined. Run db.connect."),
			  dvr);
	if (P_Drop_Aux_Table(driver, table_name) != DB_OK)
	    G_fatal_error(_("Old auxiliar table could not be dropped"));
	db_close_database_shutdown_driver(driver);
    }

    /* Open input vector */
    if ((mapset = G_find_vector2(in_opt->answer, "")) == NULL)
	G_fatal_error(_("Vector map <%s> not found"), in_opt->answer);

    Vect_set_open_level(1);	/* WITHOUT TOPOLOGY */
    if (1 > Vect_open_old(&In, in_opt->answer, mapset))
	G_fatal_error(_("Unable to open vector map <%s> at the topological level"),
		      in_opt->answer);

    /* check availability of z values
     * column option overrrides 3D z coordinates */
    if (!Vect_is_3d(&In) && (bspline_field <= 0 || bspline_column == NULL))
	G_fatal_error(_("Need either 3D vector or layer and column with z values"));
    if (bspline_field > 0 && bspline_column == NULL)
	G_fatal_error(_("Layer but not column with z values given"));

    /* Estimate point density and mean distance for current region */
    if (spline_step_flag->answer) {
	double dens, dist;
	if (P_estimate_splinestep(&In, &dens, &dist) == 0) {
	    G_message("Estimated point density: %.4g", dens);
	    G_message("Estimated mean distance between points: %.4g", dist);
	}
	else
	    G_warning(_("No points in current region!"));
	
	Vect_close(&In);
	exit(EXIT_SUCCESS);
    }

    /*----------------------------------------------------------------*/
    /* Cross-correlation begins */
    if (cross_corr_flag->answer) {
	G_debug(1, "CrossCorrelation()");
	cross = cross_correlation(&In, passoE, passoN);

	if (cross != TRUE)
	    G_fatal_error(_("Cross validation didn't finish correctly"));
	else {
	    G_debug(1, "Cross validation finished correctly");

	    Vect_close(&In);

	    G_done_msg(_("Cross validation finished for sie = %f and sin = %f"), passoE, passoN);
	    exit(EXIT_SUCCESS);
	}
    }

    /* Open input ext vector */
    if (!in_ext_opt->answer) {
	ext = FALSE;
	G_message(_("No vector map of sparse points to interpolate was specified. "
		    "Interpolation will be done with <%s> vector map"),
		  in_opt->answer);
    }
    else {
	ext = TRUE;
	G_message(_("Vector map <%s> of sparse points will be interpolated"),
		  in_ext_opt->answer);

	if ((mapset = G_find_vector2(in_ext_opt->answer, "")) == NULL)
	    G_fatal_error(_("Vector map <%s> not found"), in_ext_opt->answer);

	Vect_set_open_level(1);	/* WITHOUT TOPOLOGY */
	if (1 > Vect_open_old(&In_ext, in_ext_opt->answer, mapset))
	    G_fatal_error(_("Unable to open vector map <%s> at the topological level"),
			  in_opt->answer);
    }

    /* Open output map */
    /* vector output */
    if (vector && !map) {
	if (strcmp(dvr, "dbf") == 0)
	    G_fatal_error(_("Sorry, <%s> driver is not allowed for vector output in this module. "
			   "Try with a raster output or other driver."), dvr);

	Vect_check_input_output_name(in_opt->answer, out_opt->answer,
				     GV_FATAL_EXIT);
	grid = FALSE;

	if (0 > Vect_open_new(&Out, out_opt->answer, WITH_Z))
	    G_fatal_error(_("Unable to create vector map <%s>"),
			  out_opt->answer);

	/* Copy vector Head File */
	if (ext == FALSE) {
	    Vect_copy_head_data(&In, &Out);
	    Vect_hist_copy(&In, &Out);
	}
	else {
	    Vect_copy_head_data(&In_ext, &Out);
	    Vect_hist_copy(&In_ext, &Out);
	}
	Vect_hist_command(&Out);
    }

    /* raster output */
    raster = -1;
    G_set_fp_type(DCELL_TYPE);
    if (!vector && map) {
	grid = TRUE;
	if ((raster = G_open_fp_cell_new(out_map_opt->answer)) < 0)
	    G_fatal_error(_("Unable to create raster map <%s>"),
			  out_map_opt->answer);
    }

    /* read z values from attribute table */
    if (bspline_field > 0) {
	db_CatValArray_init(&cvarr);
	Fi = Vect_get_field(&In, bspline_field);
	if (Fi == NULL)
	    G_fatal_error(_("Cannot read field info"));

	driver_cats = db_start_driver_open_database(Fi->driver, Fi->database);
	/*G_debug (0, _("driver=%s db=%s"), Fi->driver, Fi->database); */

	if (driver_cats == NULL)
	    G_fatal_error(_("Unable to open database <%s> by driver <%s>"),
			  Fi->database, Fi->driver);

	nrec =
	    db_select_CatValArray(driver_cats, Fi->table, Fi->key,
				  col_opt->answer, NULL, &cvarr);
	G_debug(3, "nrec = %d", nrec);

	ctype = cvarr.ctype;
	if (ctype != DB_C_TYPE_INT && ctype != DB_C_TYPE_DOUBLE)
	    G_fatal_error(_("Column type not supported"));

	if (nrec < 0)
	    G_fatal_error(_("Unable to select data from table"));

	G_message(_("[%d] records selected from table"), nrec);

	db_close_database_shutdown_driver(driver_cats);
    }

    /*----------------------------------------------------------------*/
    /* Interpolation begins */
    G_debug(1, "Interpolation()");

    /* Open driver and database */
    driver = db_start_driver_open_database(dvr, db);
    if (driver == NULL)
	G_fatal_error(_("No database connection for driver <%s> is defined. "
			"Run db.connect."), dvr);

    /* Create auxiliar table */
    if (vector) {
	if ((flag_auxiliar = P_Create_Aux4_Table(driver, table_name)) == FALSE) {
	    P_Drop_Aux_Table(driver, table_name);
	    G_fatal_error(_("Interpolation: Creating table: "
			    "It was impossible to create table <%s>."),
			  table_name);
	}
	db_create_index2(driver, table_name, "ID");
	/* sqlite likes that */
	db_close_database_shutdown_driver(driver);
	driver = db_start_driver_open_database(dvr, db);
    }

    /* Setting regions and boxes */
    G_debug(1, "Interpolation: Setting regions and boxes");
    G_get_window(&original_reg);
    G_get_window(&elaboration_reg);
    Vect_region_box(&elaboration_reg, &overlap_box);
    Vect_region_box(&elaboration_reg, &general_box);

    nrows = G_window_rows();
    ncols = G_window_cols();

    /* Alloc raster matrix */
    if (grid == TRUE) {
	if (!(raster_matrix = G_alloc_matrix(nrows, ncols)))
	    G_fatal_error(_("Cannot allocate memory for auxiliar matrix."
			    "Consider changing region resolution"));
    }

    /*------------------------------------------------------------------
      | Subdividing and working with tiles: 									
      | Each original region will be divided into several subregions. 
      | Each one will be overlaped by its neighbouring subregions. 
      | The overlapping is calculated as a fixed OVERLAP_SIZE times
      | the largest spline step plus 2 * orlo
      ----------------------------------------------------------------*/

    /* Fixing parameters of the elaboration region */
    P_zero_dim(&dims);		/* Set dim struct to zero */

    nsplx_adj = NSPLX_MAX;
    nsply_adj = NSPLY_MAX;
    if (passoN > passoE)
	dims.overlap = OVERLAP_SIZE * passoN;
    else
	dims.overlap = OVERLAP_SIZE * passoE;
    P_get_orlo(bilin, &dims, passoE, passoN);
    P_set_dim(&dims, passoE, passoN, &nsplx_adj, &nsply_adj);

    G_verbose_message(_("adjusted EW splines %d"), nsplx_adj);
    G_verbose_message(_("adjusted NS splines %d"), nsply_adj);

    /* calculate number of subregions */
    orloE = dims.latoE - dims.overlap - 2 * dims.orlo_v;
    orloN = dims.latoN - dims.overlap - 2 * dims.orlo_h;

    N_extension = original_reg.north - original_reg.south;
    E_extension = original_reg.east - original_reg.west;

    nsubregion_col = ceil(E_extension / orloE) + 0.5;
    nsubregion_row = ceil(N_extension / orloN) + 0.5;

    if (nsubregion_col < 0)
	nsubregion_col = 0;
    if (nsubregion_row < 0)
	nsubregion_row = 0;

    nsubregions = nsubregion_row * nsubregion_col;

    /* Creating line and categories structs */
    points = Vect_new_line_struct();
    Cats = Vect_new_cats_struct();
    Vect_cat_set(Cats, 1, 0);

    subregion_row = 0;
    elaboration_reg.south = original_reg.north;
    last_row = FALSE;

    while (last_row == FALSE) {	/* For each subregion row */
	subregion_row++;
	P_set_regions(&elaboration_reg, &general_box, &overlap_box, dims,
		      GENERAL_ROW);

	if (elaboration_reg.north > original_reg.north) {	/* First row */

	    P_set_regions(&elaboration_reg, &general_box, &overlap_box, dims,
			  FIRST_ROW);
	}

	if (elaboration_reg.south <= original_reg.south) {	/* Last row */

	    P_set_regions(&elaboration_reg, &general_box, &overlap_box, dims,
			  LAST_ROW);
	    last_row = TRUE;
	}

	nsply =
	    ceil((elaboration_reg.north -
		  elaboration_reg.south) / passoN) + 0.5;
	G_debug(1, "Interpolation: nsply = %d", nsply);
	/*
	if (nsply > NSPLY_MAX)
	    nsply = NSPLY_MAX;
	*/
	elaboration_reg.east = original_reg.west;
	last_column = FALSE;
	subregion_col = 0;

	while (last_column == FALSE) {	/* For each subregion column */
	    int npoints = 0;

	    subregion_col++;
	    subregion++;
	    if (nsubregions > 1)
		G_message(_("subregion %d of %d"), subregion, nsubregions);

	    P_set_regions(&elaboration_reg, &general_box, &overlap_box, dims,
			  GENERAL_COLUMN);

	    if (elaboration_reg.west < original_reg.west) {	/* First column */

		P_set_regions(&elaboration_reg, &general_box, &overlap_box,
			      dims, FIRST_COLUMN);
	    }

	    if (elaboration_reg.east >= original_reg.east) {	/* Last column */

		P_set_regions(&elaboration_reg, &general_box, &overlap_box,
			      dims, LAST_COLUMN);
		last_column = TRUE;
	    }
	    nsplx =
		ceil((elaboration_reg.east -
		      elaboration_reg.west) / passoE) + 0.5;
	    G_debug(1, "Interpolation: nsplx = %d", nsplx);
	    /*
	    if (nsplx > NSPLX_MAX)
		nsplx = NSPLX_MAX;
	    */
	    G_debug(1, "Interpolation: (%d,%d): subregion bounds",
		    subregion_row, subregion_col);
	    G_debug(1, "Interpolation: \t\tNORTH:%.2f\t",
		    elaboration_reg.north);
	    G_debug(1, "Interpolation: WEST:%.2f\t\tEAST:%.2f",
		    elaboration_reg.west, elaboration_reg.east);
	    G_debug(1, "Interpolation: \t\tSOUTH:%.2f",
		    elaboration_reg.south);

	    /* reading points in interpolation region */
	    dim_vect = nsplx * nsply;
	    observ =
		P_Read_Vector_Region_Map(&In, &elaboration_reg, &npoints,
					 dim_vect, bspline_field);
	    G_debug(1,
		    "Interpolation: (%d,%d): Number of points in <elaboration_box> is %d",
		    subregion_row, subregion_col, npoints);

	    if (npoints > 0) {	/*  */
		int i;

		nparameters = nsplx * nsply;
		BW = P_get_BandWidth(bilin, nsply);

		/* Least Squares system */
		N = G_alloc_matrix(nparameters, BW);	/* Normal matrix */
		TN = G_alloc_vector(nparameters);	/* vector */
		parVect = G_alloc_vector(nparameters);	/* Parameters vector */
		obsVect = G_alloc_matrix(npoints, 3);	/* Observation vector */
		Q = G_alloc_vector(npoints);	/* "a priori" var-cov matrix */
		lineVect = G_alloc_ivector(npoints);	/*  */

		for (i = 0; i < npoints; i++) {	/* Setting obsVect vector & Q matrix */
		    double dval;

		    Q[i] = 1;	/* Q=I */
		    lineVect[i] = observ[i].lineID;
		    obsVect[i][0] = observ[i].coordX;
		    obsVect[i][1] = observ[i].coordY;

		    /* read z coordinates from attribute table */
		    if (bspline_field > 0) {
			int cat, ival, ret;

			cat = observ[i].cat;
			if (cat < 0)
			    continue;

			if (ctype == DB_C_TYPE_INT) {
			    ret =
				db_CatValArray_get_value_int(&cvarr, cat,
							     &ival);
			    obsVect[i][2] = ival;
			    observ[i].coordZ = ival;
			}
			else {	/* DB_C_TYPE_DOUBLE */
			    ret =
				db_CatValArray_get_value_double(&cvarr, cat,
								&dval);
			    obsVect[i][2] = dval;
			    observ[i].coordZ = dval;
			}
			if (ret != DB_OK) {
			    G_warning(_("Interpolation: (%d,%d): No record for point (cat = %d)"),
				      subregion_row, subregion_col, cat);
			    continue;
			}
		    }
		    /* use z coordinates of 3D vector */
		    else {
			obsVect[i][2] = observ[i].coordZ;
		    }
		}

		/* Mean calculation for every point */
		mean = P_Mean_Calc(&elaboration_reg, observ, npoints);

		G_debug(1, "Interpolation: (%d,%d): mean=%lf",
			subregion_row, subregion_col, mean);

		G_free(observ);

		for (i = 0; i < npoints; i++)
		    obsVect[i][2] -= mean;

		/* Bilinear interpolation */
		if (bilin) {
		    G_debug(1,
			    "Interpolation: (%d,%d): Bilinear interpolation...",
			    subregion_row, subregion_col);
		    normalDefBilin(N, TN, Q, obsVect, passoE, passoN, nsplx,
				   nsply, elaboration_reg.west,
				   elaboration_reg.south, npoints,
				   nparameters, BW);
		    nCorrectGrad(N, lambda, nsplx, nsply, passoE, passoN);
		}
		/* Bicubic interpolation */
		else {
		    G_debug(1,
			    "Interpolation: (%d,%d): Bicubic interpolation...",
			    subregion_row, subregion_col);
		    normalDefBicubic(N, TN, Q, obsVect, passoE, passoN, nsplx,
				     nsply, elaboration_reg.west,
				     elaboration_reg.south, npoints,
				     nparameters, BW);
		    nCorrectGrad(N, lambda, nsplx, nsply, passoE, passoN);
		}

		tcholSolve(N, TN, parVect, nparameters, BW);

		G_free_matrix(N);
		G_free_vector(TN);
		G_free_vector(Q);

		if (grid == TRUE) {	/* GRID INTERPOLATION ==> INTERPOLATION INTO A RASTER */
		    G_debug(1, "Interpolation: (%d,%d): Regular_Points...",
			    subregion_row, subregion_col);
		    raster_matrix =
			P_Regular_Points(&elaboration_reg, general_box,
					 overlap_box, raster_matrix, parVect,
					 passoN, passoE, dims.overlap, mean,
					 nsplx, nsply, nrows, ncols, bilin);
		}
		else {		/* OBSERVATION POINTS INTERPOLATION */
		    if (ext == FALSE) {
			G_debug(1, "Interpolation: (%d,%d): Sparse_Points...",
				subregion_row, subregion_col);
			P_Sparse_Points(&Out, &elaboration_reg, general_box,
					overlap_box, obsVect, parVect,
					lineVect, passoE, passoN,
					dims.overlap, nsplx, nsply, npoints,
					bilin, Cats, driver, mean,
					table_name);
		    }
		    else {	/* FLAG_EXT == TRUE */
			int npoints_ext, *lineVect_ext = NULL;
			double **obsVect_ext;	/*, mean_ext = .0; */
			struct Point *observ_ext;

			observ_ext =
			    P_Read_Vector_Region_Map(&In_ext,
						     &elaboration_reg,
						     &npoints_ext, dim_vect,
						     1);

			obsVect_ext = G_alloc_matrix(npoints_ext, 3);	/* Observation vector_ext */
			lineVect_ext = G_alloc_ivector(npoints_ext);

			for (i = 0; i < npoints_ext; i++) {	/* Setting obsVect_ext vector & Q matrix */
			    obsVect_ext[i][0] = observ_ext[i].coordX;
			    obsVect_ext[i][1] = observ_ext[i].coordY;
			    obsVect_ext[i][2] = observ_ext[i].coordZ - mean;
			    lineVect_ext[i] = observ_ext[i].lineID;
			}

			G_free(observ_ext);

			G_debug(1, "Interpolation: (%d,%d): Sparse_Points...",
				subregion_row, subregion_col);
			P_Sparse_Points(&Out, &elaboration_reg, general_box,
					overlap_box, obsVect_ext, parVect,
					lineVect_ext, passoE, passoN,
					dims.overlap, nsplx, nsply,
					npoints_ext, bilin, Cats, driver,
					mean, table_name);

			G_free_matrix(obsVect_ext);
			G_free_ivector(lineVect_ext);
		    }		/* END FLAG_EXT == TRUE */
		}		/* END GRID == FALSE */
		G_free_vector(parVect);
		G_free_matrix(obsVect);
		G_free_ivector(lineVect);
	    }
	    else {
		G_free(observ);
		G_warning(_("No data within this subregion. "
			    "Consider changing the spline step."));
	    }
	}			/*! END WHILE; last_column = TRUE */
    }				/*! END WHILE; last_row = TRUE */

    G_verbose_message(_("Writing output..."));
    /* Writing the output raster map */
    if (grid == TRUE) {
	P_Aux_to_Raster(raster_matrix, raster);
	G_free_matrix(raster_matrix);
    }
    /* Writing to the output vector map the points from the overlapping zones */
    else if (flag_auxiliar == TRUE) {
	if (ext == FALSE)
	    P_Aux_to_Vector(&In, &Out, driver, table_name);
	else
	    P_Aux_to_Vector(&In_ext, &Out, driver, table_name);

	/* Dropping auxiliar table */
	G_debug(1, "%s: Dropping <%s>", argv[0], table_name);
	if (P_Drop_Aux_Table(driver, table_name) != DB_OK)
	    G_fatal_error(_("Auxiliar table could not be dropped"));
    }

    db_close_database_shutdown_driver(driver);

    Vect_close(&In);
    if (ext != FALSE)
	Vect_close(&In_ext);
    if (vector)
	Vect_close(&Out);

    if (map) {
	G_close_cell(raster);

	/* set map title */
	sprintf(title, "%s interpolation with Tykhonov regularization",
		type_opt->answer);
	G_put_cell_title(out_map_opt->answer, title);
	/* write map history */
	G_short_history(out_map_opt->answer, "raster", &history);
	G_command_history(&history);
	G_write_history(out_map_opt->answer, &history);
    }

    G_done_msg(" ");

    exit(EXIT_SUCCESS);
}				/*END MAIN */
