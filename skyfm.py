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
        r.append(obj.group(1))
count = 0
for num in range(len(r)):
    obj = re.search(r'"id":([\d]+),"key":"([\s\S]+)","name":"([\s\S]+)","description":"([\s\S]+)","playlist":"([\s\S]+)"', r[num])
    if obj:
        print "#%d SKYFM id:"%count,obj.group(1),",","name:",obj.group(3),",",obj.group(4)
#        print "mplayer -ao oss -cache 256 -playlist ", obj.group(5), " < /dev/null &"
        print obj.group(5)
        count = count + 1
