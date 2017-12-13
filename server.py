#!/usr/bin/python3

from socket import *
import threading
import sys
import locale, datetime
import time
import os

DEFAULT_PORT = 10000

def readClient(csock):
  try:
    while (1):
      message = csock.recv(1024)
      message = message.decode()
      print(message)
      if len(message) == 0: 
        raise Exception("Client closed unexpectedly")
  except:
    csock.close()

def sendClient(csock):
  csock.send("Ping packet".encode())
              
def main(serverPort):
  serverSocket = socket(AF_INET, SOCK_STREAM)
  serverSocket.bind(('localhost',serverPort))
  serverSocket.listen(5)
  print('Ready to serve on port',serverPort)
  try:
    while True:
      connectionSocket, addr = serverSocket.accept()
      print("serverSocket accepted")
      connectionSocket.send("You are now connected to the server".encode())
      workerThread = threading.Thread(target = readClient, args=(connectionSocket,))
      workerThread.start()
      workerThread2 = threading.Thread(target = sendClient, args=(connectionSocket,)) 
      workerThread2.start()

  except KeyboardInterrupt:
    connectionSocket.send("Server shutting down now! Thanks for pinging!\n".encode())
    serverSocket.close()
    workerThread.join()
        
    print("Shutdown complete... exiting")
    sys.exit()
                  
       
if __name__ == "__main__":
  servPort = DEFAULT_PORT
  main(servPort)

