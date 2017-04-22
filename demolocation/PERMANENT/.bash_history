v.unpack country_boundaries.pack 
g.proj -w
v.unpack country_boundaries.pack -v
v.unpack country_boundaries.pack --v
g.proj -w
g.proj -p
cd grass72/demolocation/PERMANENT/
pwd
meld PROJ_INFO ~/grassdata/ll/PERMANENT/PERMANENT/PROJ_INFO 
cp ~/grassdata/ll/PERMANENT/PERMANENT/PROJ_INFO .
svn diff
cat PROJ_
cat PROJ_INFO 
cat PROJ_UNITS Ã
cat PROJ_UNITS
ccat ~/grassdata/ll/PERMANENT/PERMANENT/PROJ_UNITS 
cat ~/grassdata/ll/PERMANENT/PERMANENT/PROJ_UNITS 
svn ci -m"demolocation: update to current file structure as generated with 'grass72 -c EPSG:4326 ~/grassdata/ll/PERMANENT'" PROJ_INFO 
v.unpack country_boundaries.pack --v
l /home/neteler/grass72/demolocation/PERMANENT/
cd grass72/demolocation/PERMANENT/
mkdir sqlite
cd
v.unpack country_boundaries.pack --v
v.info country_boundaries
v.db.connect -p country_boundaries
g.region -p
g.gui
v.info -c country_boundaries
v.unpack country_boundaries.pack
v.info map=country_boundaries@PERMANENT
g.region -p
v.db.connect -p country_boundaries
v.build.all 
g.gisenv 
v.split g
v.split -n box_4_corners output=box_4_corners_many_vertices length=200 units=kilometers
g.region -p
v.split -n box_4_corners output=box_4_corners_many_vertices length=0.2
v.split -n box_4_corners output=box_4_corners_many_vertices length=0.2 --o
v.split -n box_4_corners output=box_4_corners_many_vertices length=200 units=kilometers
v.split -n box_4_corners output=box_4_corners_many_vertices length=200 units=kilometers --o
g.list vect
g.remove vect=box_4_corners box_4_corners_many_vertices
g.remove vect=box_4_corners,box_4_corners_many_vertices
