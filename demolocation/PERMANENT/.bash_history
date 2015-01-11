db.connect -p
g.manual 
g.manual v.db.reconnect.all
v.db.reconnect.all old_database='$GISDBASE/$LOCATION_NAME/$MAPSET/dbf/'  new_driver=sqlite new_database='$GISDBASE/$LOCATION_NAME/$MAPSET/sqlite/sqlite.db'
v.build.all 
v.db.reconnect.all old_database='$GISDBASE/$LOCATION_NAME/$MAPSET/dbf/'  new_driver=sqlite new_database='$GISDBASE/$LOCATION_NAME/$MAPSET/sqlite/sqlite.db'
db.connect -p
db.connect driver=sqlite database='$GISDBASE/$LOCATION_NAME/$MAPSET/sqlite/sqlite.db'
db.connect -p
db.tables -p
l /home/neteler/grass70/demolocation/PERMANENT/sqlite/sqlite.db
l /home/neteler/grass70/demolocation/PERMANENT/sqlite/
l /home/neteler/grass70/demolocation/PERMANENT/
db.connect -p
v.db.reconnect.all old_database='$GISDBASE/$LOCATION_NAME/$MAPSET/dbf/'  new_driver=sqlite new_database='$GISDBASE/$LOCATION_NAME/$MAPSET/sqlite/sqlite.db'
l /home/neteler/grass70/demolocation/PERMANENT/sqlite/sqlite.db
l /home/neteler/grass70/demolocation/PERMANENT/sqlite/
mkdir /home/neteler/grass70/demolocation/PERMANENT/sqlite/
v.db.reconnect.all old_database='$GISDBASE/$LOCATION_NAME/$MAPSET/dbf/'  new_driver=sqlite new_database='$GISDBASE/$LOCATION_NAME/$MAPSET/sqlite/sqlite.db'
cd demolocation/
l
cd PERMANENT/
l
svn status
svn revert VAR vector
svn revert vector
svn revert VAR vector/*
svn status
svn revert VAR vector/*/*
svn status
rm -f vector/mysites/sidx vector/mysites/sidx
l
v.build.all 
rm -f sqlite/sqlite.db 
v.db.reconnect.all old_database='$GISDBASE/$LOCATION_NAME/$MAPSET/dbf/'  new_driver=sqlite new_database='$GISDBASE/$LOCATION_NAME/$MAPSET/sqlite/sqlite.db'
db.connect driver=sqlite database='$GISDBASE/$LOCATION_NAME/$MAPSET/sqlite/sqlite.db'
db.tables -p
l
history 
svn revert VAR vector/*/*
svn status
rm -rf sqlite vector/mysites/sidx vector/point/sidx
svn status
