# (c)opyright 2017 rivan juthani | Made purly in python
# remoteipgraber-client.py | 2017 updated & api version 0.2.7
#!/usr/bin/env python

import socket

s = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
host = [server-host]
port = [port-number]
s.connect((host, port))
tm = s.recv(1024)
s.close()
