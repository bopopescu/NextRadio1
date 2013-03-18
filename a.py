import socket
import re
import os 
import subprocess
i = 0
stationlist=[]
fd = open ("/root/radio.txt","r")
for line in fd:
    msg = re.search('^#',line)
    if msg:
       print "...."
    else:
       stationlist.append(line)
       i = i+1
fd.close()
max_stations = i
print i
print stationlist[0]
current_station = 0
player = subprocess.Popen(stationlist[current_station].split(" "))
sockfile = '/dev/lircd'
client_socket = socket.socket(socket.AF_UNIX, socket.SOCK_STREAM)
client_socket.connect(sockfile);
funkey = 0

def ProcessKey( current_station ):
    station_num = 0
    funckey = 0
    while 1:
        data = client_socket.recv( 512 )
        cmd_list = data.split( " " )
        if ( cmd_list[1] == "00" ):
            if ( cmd_list[2][0] == 'D' ):
               station_number = funckey + int ( cmd_list[2][1] )
               funckey = 0
               return station_number
            elif ( cmd_list[2][0] == 'R' ):
                funckey = 10
            elif ( cmd_list[2][0] == 'G' ):
                funckey = 20
            elif ( cmd_list[2][0] == 'Y' ):
                funckey = 30
            elif ( cmd_list[2][0] == 'B' ):
                funckey = 40
            elif ( cmd_list[2] == "chUp" or cmd_list[2] == "chUp_V2" ):
                return current_station + 1
            elif ( cmd_list[2] == "chDown" or cmd_list[2] == "chDown_V2"):
                return current_station -1
                

def PlayRadio( station ):
       os.system("killall " + "mplayer");
       current_station = station
       print current_station
       player = subprocess.Popen(stationlist[current_station].split(" "))

                

while 1:
    station = ProcessKey( current_station )
    if ( station == current_station):
       continue
    elif ( station > max_stations +1 ):
       continue
    elif ( station == max_stations ):
       station = 0;
    elif ( station < 0 ):
       station = max_stations -1
    current_station = station
    PlayRadio ( current_station )
