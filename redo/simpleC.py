#!/usr/bin/python3
import sys
from socket import *
import threading

serverName = ''
serverPort = 10000
clientsocket = socket(AF_INET, SOCK_STREAM)
print("socket created")
clientsocket.connect((serverName, serverPort))
print("Connection achieved")
message = clientsocket.recv(1024)
message = message.decode()
print(message)
clientsocket.send('hello'.encode())
