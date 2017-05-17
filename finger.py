#!/usr/bin/python

import socket
import re

# open listen socket
serversocket = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
serversocket.setsockopt(socket.SOL_SOCKET, socket.SO_REUSEADDR, 1)
serversocket.bind(('localhost', 8089))
serversocket.listen(5) # become a server socket, maximum 5 connections

# read user data, handle timeouts.
# check that completed data ends with CR/LF
# return line for parsing or None
def getreq(c):
    l = c.recv(2048)
    sz = len(l)
    if l[sz-2:] != "\r\n":
        return None
    return l

class userreq:
    def __init__(self):
        self.verbose = False
        self.user = None
        self.hostlist = None

def reqparse(l):
    req = userreq()
    if (l[:2] == '\\W'):
        l = l[2:]           # strip off /W
        req.verbose = True
        print "verbose"
    m = re.match('\s*([^@]+)', l)
    if (m is not None):
        req.user = m.group(1)
    print "User", req.user
    return req

while True:
  c, addr = serversocket.accept()
  print "connection from", addr
  l = getreq(c)
  print "have", l
  r = reqparse(l)

  if (r is None):
      print "Error"
  elif (r.hostlist is not None):
      print "Q2"
  else:
      if (r.user is None):
          print "General"
      else:
          print "specific"
  # Q1= nothing, space then username

  # Q2 = space, username, hostname(multiple as wanted)

  # if parse fails, return None

  #need to parse l, for line.



  c.close()
