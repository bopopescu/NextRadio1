#-*- coding: utf-8 -*-
#############################################
#
# Python script renumber playlist (renum.py)
# Version: 1.1
#
# Created by Aladdin
#
# Changes Logs:
# [2013-04-23] By Aladdin
#              re-number playlist of NextRadio


import re
from sys import argv
script, filename = argv
i = 0
fd = open (filename, "r")
for line in fd:
    msg = re.search('^#[\d]+', line)
    if msg:
        line = re.sub('^#[\d]+','#' + str(i),line)
        i = i+1
    print line.rstrip("\n")
fd.close()
