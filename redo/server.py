#!/usr/bin/python3
from socket import *
import threading
import sys
import locale, datetime
import time
import os

def readFromClient():
    while True:
         data = s.recv(1024)
         if not data: sys.exit(0)
         print data

def sentToClient(cS):
  while True:
    newMesage = input("Enter message: ")
    #cS.send(newMessage.encode())

def main():
  serverName = 'localhost'
  serverPort = 10000
  threads = []
  sS = socket(AF_INET, SOCK_STREAM)
  print("Socket created")
  sS.bind((serverName,serverPort))
  print("Bind complete")
  sS.listen(5)

  try:
    while True:
      cS, addr = sS.accept()
      print('Connected with ' + addr[0] + ':' + str(addr[1]))
      buf = cS.recv(64)
      if len(buf) > 0:
        print(buf.decode())
        break
      cS.send('hello client!'.encode())
          #workerThread = threading.Thread(target = readFromClient, args = (cS, ))
    #senderThread = threading.Thread(target = sentToClient, args = (cS, ))
    #workerThread.start()
    #senderThread.start()
  except KeyboardInterrupt:
    cS.close()
    sS.close()
    #workerThread.join()
    #senderThread.join()
    sys.exit()
                    
       
if __name__ == "__main__":
  main()

