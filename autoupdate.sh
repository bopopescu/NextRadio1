#!/bin/sh
# file: autoupdate.sh
#

#
WGET='/usr/bin/wget --no-check-certificate -N'

# Updating the a.py
URL='https://github.com/sp0500/NextRadio/raw/master/a.py'
$WGET $URL
[ $? = 0 ] && echo "Updating the file a.py Done."

# Adding the updated scripts for NextRadio to the following
