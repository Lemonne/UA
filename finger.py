#!/usr/bin/python

import socket
# open listen socket
serversocket = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
serversocket.setsockopt(socket.SOL_SOCKET, socket.SO_REUSEADDR, 1)
serversocket.bind(('localhost', 8089))
serversocket.listen(5) # become a server socket, maximum 5 connections

while True:
  c, addr = serversocket.accept()
  print "connection from", addr
  l = c.recv(2048)
  print "have", l
  

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
