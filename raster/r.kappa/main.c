
/****************************************************************************
 *
 * MODULE:       r.kappa
 * AUTHOR(S):    Tao Wen, UIUC (original contributor)
 *               Markus Neteler <neteler itc.it>,
 *               Roberto Flor <flor itc.it>, 
 *               Bernhard Reiter <bernhard intevation.de>, 
 *               Brad Douglas <rez touchofmadness.com>, 
 *               Glynn Clements <glynn gclements.plus.com>, 
 *               Jachym Cepicky <jachym les-ejk.cz>, 
 *               Jan-Oliver Wagner <jan intevation.de>
 * PURPOSE:      tabulates the error matrix of classification result by
 *               crossing classified map layer with respect to reference map 
 *               layer
 * COPYRIGHT:    (C) 1999-2006 by the GRASS Development Team
 *
 *               This program is free software under the GNU General Public
 *               License (>=v2). Read the file COPYING that comes with GRASS
 *               for details.
 *
 *****************************************************************************/
#include <stdlib.h>
#include <stdio.h>
#include <string.h>
#include <grass/gis.h>
#include <grass/glocale.h>
#include "local_proto.h"
#include "kappa.h"

struct Cell_head window;

char *maps[2];
char *output;
char *title;
long *matr;
long *rlst;
int ncat;
char *stats_file;

LAYER *layers;
int nlayers;

GSTATS *Gstats;
size_t nstats;

/* function prototypes */
static void layer(char *s);

int main(int argc, char **argv)
{
    int i;
    struct GModule *module;
    struct
    {
	struct Option *map, *ref, *output, *titles;
    } parms;

    struct
    {
	struct Flag *n, *w, *q, *h;
    } flags;

    G_gisinit(argv[0]);

    module = G_define_module();
    module->keywords = _("raster, statistics");
    module->description =
	_("Calculate error matrix and kappa "
	  "parameter for accuracy assessment of classification " "result.");

    parms.map = G_define_standard_option(G_OPT_R_INPUT);
    parms.map->key = "classification";
    parms.map->description =
	_("Name of raster map containing classification result");

    parms.ref = G_define_standard_option(G_OPT_R_INPUT);
    parms.ref->key = "reference";
    parms.ref->description =
	_("Name of raster map containing reference classes");

    parms.output = G_define_standard_option(G_OPT_F_OUTPUT);
    parms.output->required = NO;
    parms.output->description =
	_("Name for output file containing error matrix and kappa");

    parms.titles = G_define_option();
    parms.titles->key = "title";
    parms.titles->type = TYPE_STRING;
    parms.titles->required = NO;
    parms.titles->description = _("Title for error matrix and kappa");
    parms.titles->answer = "ACCURACY ASSESSMENT";

    flags.w = G_define_flag();
    flags.w->key = 'w';
    flags.w->label = _("Wide report");
    flags.w->description = _("132 columns (default: 80)");

    /* please, remove before GRASS 7 released */
    flags.q = G_define_flag();
    flags.q->key = 'q';
    flags.q->description = _("Quiet");

    flags.h = G_define_flag();
    flags.h->key = 'h';
    flags.h->description = _("No header in the report");

    if (G_parser(argc, argv))
	exit(EXIT_FAILURE);

    G_get_window(&window);

    maps[0] = parms.ref->answer;
    maps[1] = parms.map->answer;
    for (i = 0; i < 2; i++)
	layer(maps[i]);

    output = parms.output->answer;

    title = parms.titles->answer;

    /* please, remove before GRASS 7 released */
    if (flags.q->answer) {
	G_putenv("GRASS_VERBOSE", "0");
	G_warning(_("The '-q' flag is superseded and will be removed "
		    "in future. Please use '--quiet' instead"));
    }

    /* run r.stats to obtain statistics of map layers */
    stats();

    /* print header of the output */
    if (!flags.h->answer)
	prn_header();

    /* prepare the data for calculation */
    prn_error_mat(flags.w->answer ? 132 : 80, flags.h->answer);

    /* generate the error matrix, kappa and variance */
    calc_kappa();

    return EXIT_SUCCESS;
}


static void layer(char *s)
{
    char name[GNAME_MAX], *mapset;
    int n;

    strcpy(name, s);
    if ((mapset = G_find_cell2(name, "")) == NULL)
	G_fatal_error(_("Raster map <%s> not found"), s);

    n = nlayers++;
    layers = (LAYER *) G_realloc(layers, 2 * sizeof(LAYER));
    layers[n].name = G_store(name);
    layers[n].mapset = mapset;
    G_read_cats(name, mapset, &layers[n].labels);
}
