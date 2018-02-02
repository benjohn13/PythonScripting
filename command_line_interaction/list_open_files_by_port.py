# It’s not uncommon for a process to run on a server and listen to a port. 
# Unfortunately, you sometimes don’t want that process to keep running, but 
# all you know is the port that you want to free up. You’re going to write a 
# script to make it easy to get rid of those pesky processes.

# Creating a script that takes a port_number as its only argument 
# Calls out to 'lsof' to determine if there is a process listening on that port

#!/usr/bin/env python

import subprocess
import os
from argparse import ArgumentParser

parser = ArgumentParser(description='kill the running process listening on a given port')
parser.add_argument('port', type=int, help='the port number to search for')

port = parser.parse_args().port

# If there is a process, kill the process and inform the user
# If there is no process, print that there was no process running on that port

try:
    output = subprocess.check_output(['lsof', '-n', "-i4TCP:%s" % port])
except subprocess.CalledProcessError:
    print("No process listening on port %s" % port)
else:
    listening = None

    for line in output.splitlines():
        if "LISTEN" in line:
            listening = line
            break

    if listening:
    	# Use the string split() method to break a string into a list of its words
        # PID is the second column in the output
        pid = int(listening.split()[1])
        # Chossing to use the os.kill(pid, 9) function instead of kill command
        os.kill(pid, 9)
        print("Killed process %s" % pid)
    else:
        print("No process listening on port %s" % port)


# In terminal one, server one
# bin $ python -m SimpleHTTPServer 5500
# Serving HTTP on 0.0.0.0 port 5500 ...
# bin $

# In terminal two, server one
# bin $ sudo kill-proc-port 5500
# Killed process 8626
# bin $ 
# bin $ sudo kill-proc-port 5500
# No process listening on port 5500
# bin $