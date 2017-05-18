#!/usr/bin/python

import socket
import re

PORT = 8089

# open listen socket
serversocket = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
serversocket.setsockopt(socket.SOL_SOCKET, socket.SO_REUSEADDR, 1)
serversocket.bind(('localhost', PORT))
serversocket.listen(5) # become a server socket, maximum 5 connections

# read user data, handle timeouts.
# check that completed data ends with CR/LF
# return line for parsing with CR/LF removed or None
def getreq(c):
    l = c.recv(2048)
    size = len(l)
    if l[size-2:] != "\r\n":
        return None
    return l[:size-2]

class userreq:
    def __init__(self):
        self.verbose = False
        self.user = None
        self.hostlist = None

    def addhost(self, h):
        self.hostlist = self.hostlist or []
        self.hostlist.append(h)

def reqparse(l):
    req = userreq()
    if (l[:2] == '\\W'):
        l = l[2:]           # strip off /W
        req.verbose = True
    # allow leading spaces, be liberal, allow trailing spaces.
    l = l.rstrip(' ')
    m = re.match('\s*([^@\s]+)', l)

    if (m is not None):
        req.user = m.group(1)
        l = l[m.end():]             # strip off user

    # create the host groups
    while True:
        m = re.match('@([^@\s]+)', l)
        if (m is None):
            break
        req.addhost(m.group(1))
        l = l[m.end():]
    if len(l) != 0:
        return None
    return req

def online(req):
    return "Jonathan\nNerissa\nUrbanAirship\n"

def user_lookup(req):
    data = "User " + req.user + "\n"
    if (req.verbose):
        data += "more details\n"
    return data

# uses finger to send from last @host
def forward(req):
    nextHost = req.hostlist.pop()
    if req.verbose:
        data = '\W' + req.user
    else:
        data = req.user
    for host in req.hostlist:
        data += "@" + host
    print "forward", nextHost, data
    return finger(nextHost, data)

def finger(host, data):
    s = socket.create_connection((host, PORT))
    #s.connect()
    s.write(data)
    return s.recv(2048)

# open a connection, parses string. separates requests
while True:
  c, address = serversocket.accept()
  print "connection from", address
  l = getreq(c)
  print "have", l
  r = reqparse(l)

  if (r is None):
      data = None
      print "Error"
  elif (r.hostlist is not None):
      # Q2 variant
      data = forward(r)
  else:
      if (r.user is None):
          # general online user request
          data = online(r)
      else:
          # specific user request
          data = user_lookup(r)
  if data is not None:
      c.send(data)
  c.close()
