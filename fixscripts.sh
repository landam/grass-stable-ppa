#!/bin/sh

# this script try to locate all the GRASS script than have something
# that makes lintian complain and fix them.

# make these scripts executable
for x in etc/help/17.manual/Help.pages/curcsh40 \
    tcltkgrass/main/tcltkgrass.tcl \
    tcltkgrass/main/unused/tcltkgrass_start_with_superview \
    tcltkgrass/main/unused/tcltkgrass
do
    chmod +x $CURDIR/debian/tmp/usr/lib/grass5/$x
done
#    etc/nviz2.2/scripts/panel_label.tcl \
#    etc/nviz2.2/scripts/panel_scale.tcl \
#    etc/nviz2.2/scripts/structlib.tcl \

# silence bogus lintian complaint about interpreter-not-absolute
#for x in script_get_line \
#    script_play \
#    script_tools \
#    script_file_tools \
#    nviz2.2_script
#do
#  f=$CURDIR/debian/tmp/usr/lib/grass5/etc/nviz2.2/scripts/$x
#  sed 's.!\$$(GISBASE).!/usr/lib/grass5.' $f >foo && cat foo >$f
#done
#for x in panel_label.tcl \
#    panel_mkdspf.tcl \
#    panel_scale.tcl
#do
#  f=$CURDIR/debian/tmp/usr/lib/grass5/etc/nviz2.2/scripts/$x
#  sed 's%!../glnviz.new/nvwish%!/usr/lib/grass5/etc/nviz2.2/glnviz/nvwish%' $f >foo && cat foo >$f
#done
#rm foo

# silence lintian warning executable-not-elf-or-script
for x in etc/r.fea/show.sh \
    scripts/rgb.hsv.sh \
    scripts/show.fonts.sh \
    scripts/bug.report.sh \
    scripts/hsv.rgb.sh \
    scripts/blend.sh \
    etc/paint/driver.shell \
    scripts/demo.sh \
    scripts/split.sh \
    scripts/show.color.sh \
    scripts/grass.logo.sh \
    etc/agnps50/display_cell_map.sh \
    scripts/intens.sh \
    scripts/3d.view.sh \
    etc/paint/driver.rsh \
    etc/bin/inter/r.weight \
    scripts/ps.add.pagesize \
    etc/i.oif/m.cutmatrix \
    scripts/demo.scripts/CVS/Tag \
    etc/i.oif/i.oifcalc \
    etc/paint/driver.sh/preview \
    bwidget/demo/demo.tcl \
    scripts/demo.scripts/CVS/Entries \
    scripts/v.in.arc.poly \
    scripts/demo.scripts/CVS/Repository \
    etc/copy \
    scripts/r.combine \
    etc/paint/driver.sh/preview2 \
    scripts/demo.scripts/CVS/Root \
    etc/paint/driver.uninst/ppm \
    etc/i.oif/r.stddev \
    scripts/demo.scripts/outline
do
  f=$CURDIR/debian/tmp/usr/lib/grass5/$x
  cp $f foo; echo "#!/bin/sh" >$f; cat foo >>$f
done
rm foo

