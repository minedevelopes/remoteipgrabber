# (c)opyright 2017 rivan juthani | Made purly in python
# remoteipgraber-server.py | 2017 updated & api version 0.2.7
#!/usr/bin/env python

import argparse
import requests
import socket

class bcolors:
    HEADER = '\033[94m'
    OKGREEN = '\033[92m'
    WARNING = '\033[93m'
    FAIL = '\033[91m'
    ENDC = '\033[0m'
    BOLD = '\033[1m'
    UNDERLINE = '\033[4m'

if __name__ == '__main__':
    parser = argparse.ArgumentParser()
    parser.add_argument('--starts', help='Starts the server and waits for connections[default: if you run the script it auto starts the server]', choices=['yes','YES'])
    parser.add_argument('--stops', help='Stops the server and exits the script', choices=['yes','YES'])
    arg = parser.parse_args()

    s = socket.socket()
    host = socket.gethostname()
    port = 12345
    s.bind((host, port))
    sstatus = 'Waiting/Slient'

    s.listen(5)
    print '-----------------------------------'
    print '|        Server Properties'
    print '| Server host:', host
    print '| Server port:', port
    print '| Server status:', sstatus
    print '-----------------------------------'
    print 'NOTE: Please wait while some clients connect!'
    while True:
        c, addr = s.accept()
        currentTime = time.ctime(time.time()) + "\r\n"
        print 'Got connection from client at', currentTime,'!'
        c.send(currentTime.endcode('ascii'))
        print 'Seting up ipgrab using ipg-api...'
        data = conn.recv(1024)
        print 'SERVER DATA RECEIVED:', repr(data)
        ipg = socket.gethostbyname('www.google.com')
        print 'ipgoogle =', ipg
        print 'Got server ip address:', addr
        print 'Closing the connect for NOTRACE-api...'
        c.close()
