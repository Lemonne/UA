#!/usr/bin/python

import socket
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
    if l[sz-2:] == "\r\n":
        print "CRLF"
    print "last", l[sz-2]
    return l

while True:
  c, addr = serversocket.accept()
  print "connection from", addr
  l = getreq(c)
  print "have", l
  #need to parse l, for line.



  c.close()

'''
  #seed timeout python
  end = False
  while (!timeout and !end)
    line = #collect data
    if()#the line contains the ending
        end = True
    if(!end)
        break

#parse line
'''
