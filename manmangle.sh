#!/bin/sh -e

# this script mangle the manpages included in the GRASS distributions
# to produce something usable under a debian system (my only problem is
# that GRASS uses its own system [as always *grin*] to assign pages to
# sections...)

MAN1="man1 man2 man3 man4"
MAN5="man5"
TOPDIR="`pwd`"
DESTDIR="$1"

echo Installing manpages to $DESTDIR ...
install -d $DESTDIR
install -d $DESTDIR/man1
install -d $DESTDIR/man5
cd man

# install the "section 1" manpages
echo Installing 1 manpages ...
install -m 644 utilities/man.header $DESTDIR/man1/man.header.1grass
rm -f solink
echo ".so $DESTDIR/man1/man.header.1grass" >solink
for d in $MAN1 ; do
    for f in `find $d -regex "$d/[^.].+"` ; do
	echo -n "Processing $f ... "
        cat utilities/man.version $d/.class-header solink $f $d/.class-notice \
	    >$DESTDIR/man1/`basename $f`.1grass
	echo done
    done
done

# install the "section 5" manpages
echo Installing 5 manpages ...
install -m 644 utilities/man.header $DESTDIR/man5/man.header.5grass
rm -f solink
echo ".so $DESTDIR/man5/man.header.5grass" >solink
for d in $MAN5 ; do
    for f in `find $d -regex "$d/[^.].+"` ; do
	echo -n "Processing $f ... "
        cat utilities/man.version $d/.class-header solink $f $d/.class-notice \
	    >$DESTDIR/man5/`basename $f`.1grass
	echo done
    done
done

rm -f solink
