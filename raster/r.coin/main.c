
/****************************************************************************
 *
 * MODULE:       r.coin
 *
 * AUTHOR(S):    Michael O'Shea - CERL
 *               Michael Shapiro - CERL
 *
 * PURPOSE:      Calculates the coincidence of two raster map layers.
 *
 * COPYRIGHT:    (C) 2006 by the GRASS Development Team
 *
 *               This program is free software under the GNU General Public
 *               License (>=v2). Read the file COPYING that comes with GRASS
 *               for details.
 *
 ***************************************************************************/

#include <stdlib.h>
#include <string.h>
#include <grass/gis.h>
#include <grass/glocale.h>
#include "coin.h"

struct Cell_head window;

const char *title1, *title2;

double window_cells;
double window_area;

struct stats_table *table;
long *catlist1, *catlist2;
int no_data1, no_data2;
int Rndex, Cndex;
const char *dumpname;
const char *statname;
FILE *dumpfile;

const char *mapset1, *mapset2;
const char *map1name, *map2name;
int ncat1, ncat2;

char *fill, *midline;

int main(int argc, char *argv[])
{
    struct GModule *module;
    struct
    {
	struct Option *map1, *map2, *units;
    } parm;
    struct
    {
	struct Flag *w;
    } flag;

    fill =
	"                                                                                                                                       ";
    midline =
	"------------------------------------------------------------------------------------------------------------------------------------";

    G_gisinit(argv[0]);

    module = G_define_module();
    module->keywords = _("raster");
    module->description =
	_("Tabulates the mutual occurrence (coincidence) "
	  "of categories for two raster map layers.");

    parm.map1 = G_define_option();
    parm.map1->key = "map1";
    parm.map1->required = YES;
    parm.map1->type = TYPE_STRING;
    parm.map1->gisprompt = "old,cell,raster";
    parm.map1->description = _("Name of first raster map");

    parm.map2 = G_define_option();
    parm.map2->key = "map2";
    parm.map2->required = YES;
    parm.map2->type = TYPE_STRING;
    parm.map2->gisprompt = "old,cell,raster";
    parm.map2->description = _("Name of second raster map");

    parm.units = G_define_option();
    parm.units->key = "units";
    parm.units->required = YES;
    parm.units->type = TYPE_STRING;
    parm.units->label = _("Unit of measure");
    parm.units->description =
	_("c(ells), p(ercent), x(percent of category [column]), "
	  "y(percent of category [row]), a(cres), h(ectares), "
	  "k(square kilometers), m(square miles)");
    parm.units->options = "c,p,x,y,a,h,k,m";

    flag.w = G_define_flag();
    flag.w->key = 'w';
    flag.w->description = _("Wide report, 132 columns (default: 80)");

    if (G_parser(argc, argv))
	exit(EXIT_FAILURE);

    G_get_window(&window);
    /* now make a temorary region with the same boundaries only 1 x 1 */
    window.rows = 1;
    window.cols = 1;
    G_adjust_Cell_head(&window, 1, 1);
    G_set_window(&window);

    G_begin_cell_area_calculations();
    window_area = G_area_of_cell_at_row(0);

    /* restore region back to the original */
    G_get_window(&window);
    G_set_window(&window);

    dumpname = G_tempfile();
    statname = G_tempfile();

    window_cells = G_window_rows() * G_window_cols();

    map1name = parm.map1->answer;
    map2name = parm.map2->answer;

    mapset1 = G_find_cell2(map1name, "");
    if (!mapset1)
	G_fatal_error(_("Raster map <%s> not found"), map1name);
    mapset2 = G_find_cell2(map2name, "");
    if (!mapset2)
	G_fatal_error(_("Raster map <%s> not found"), map2name);

    make_coin();
    print_coin(*parm.units->answer, flag.w->answer ? 132 : 80, 0);

    remove(dumpname);
    remove(statname);

    exit(EXIT_SUCCESS);
}
