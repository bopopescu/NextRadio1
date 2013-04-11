#!/usr/bin/python
import urllib,re
# Get a file-like object for the Python Web site's home page.
f = urllib.urlopen("http://listen.sky.fm/public1")
# Read from the object, storing the page's contents in 's'.
s = f.read()
f.close()
o = s.split("}")
r = list()

for index in range(len(o)):
  obj = re.search(r'{([\s\S]+)', o[index])
  if obj:
    s = obj.group(1).split(",")
    r.append(s)

for num in range(len(r)):
    for index in range(len(r[num])):
        if '"name"' in r[num][index]:
           name = re.search(r'"([\s\S"]+)":"([\s\S]+)"', r[num][index])
        if '"playlist"' in r[num][index]:
           url = re.search(r'"([\s\S]+)":"([\s\S]+)"', r[num][index])
    if name:
       print '#', name.group(2)
    if url:
       print "mplayer -ao oss -cache 256 -playlist ", url.group(2), " < /dev/null &"

