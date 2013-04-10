import socket
import re
import os 
import subprocess
from subprocess import Popen, PIPE
i = 0
stationlist=[]
fd = open ("/root/NextRadio/radio.txt","r")
for line in fd:
    msg = re.search('^#',line)
    if msg:
       print "."
    else:
       stationlist.append(line)
       i = i+1
fd.close()
max_stations = i
print stationlist[0]
current_station = 0
player = subprocess.Popen(stationlist[current_station].split(" ") , stdin=PIPE)
sockfile = '/dev/lircd'
client_socket = socket.socket(socket.AF_UNIX, socket.SOCK_STREAM)
client_socket.connect(sockfile);
funkey = 0
power = 1


def ProcessKey(current_station):
    station_num = 0
    funckey = 0
    while 1:
        data = client_socket.recv(512)
        cmd_list = data.split( " " )
        if (cmd_list[1] == "00"):
            if (cmd_list[2][0] == 'D'):
               station_number = funckey + int (cmd_list[2][1])
               funckey = 0
               return station_number
            elif (cmd_list[2][0] == 'R'):
                funckey = funckey + 10
            elif (cmd_list[2][0] == 'G'):
                funckey = funckey + 20
            elif (cmd_list[2][0] == 'Y'):
                funckey = funckey + 30
            elif (cmd_list[2][0] == 'B'):
                funckey = funckey + 40
            elif (cmd_list[2] == "chUp" or cmd_list[2] == "chUp_V2"):
                return current_station + 1
            elif (cmd_list[2] == "chDown" or cmd_list[2] == "chDown_V2"):
                return current_station - 1
            elif (cmd_list[2] == "volUp" or cmd_list[2] == "volUp_V2"):
                return 1000
            elif (cmd_list[2] == "volDown" or cmd_list[2] == "volDown_V2"):
                return 1100
            elif (cmd_list[2] == "power"):
                funckey = 0
                return 1200
                

def PlayRadio(station):
   if (power == 1):
       os.system("killall " + "mplayer");
       current_station = station
       print current_station
       player = subprocess.Popen(stationlist[current_station].split(" "), stdin=PIPE)

                

while 1:
    station = ProcessKey(current_station)
    if (station == 1000):
       #player.stdin.write('0')
       continue
    elif (station == 1100):
       #player.stdin.write('9')
       continue
    elif (station == 1200):
       if (power == 1):
          power = 0
          os.system("killall " + "mplayer");
       else:
          power = 1
          PlayRadio(current_station)
       continue
    elif (station == current_station):
       continue
    elif (station > max_stations +1):
       continue
    elif (station == max_stations):
       station = 0;
    elif (station < 0):
       station = max_stations -1
    PlayRadio (station)
