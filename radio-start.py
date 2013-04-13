#!/usr/bin/python
#

import os, sys

# Checking and downloading the latest updates for NextRadio
url = 'https://github.com/sp0500/NextRadio/raw/master/autoupdate.sh'
wkdir = os.path.abspath(os.path.dirname(sys.argv[0]))
file_name = url.split('/')[-1]
os.chdir(wkdir)
r = os.system("wget --no-check-certificate -N %s" %url)
if r == 0:
   print "The latest file downloaded: " + wkdir + "/" + file_name
   print "Now performing the autoupdate..."
   os.system("sh autoupdate.sh")

# Starting the Radio
print "Starting the Radio..."
os.system("python a.py")

