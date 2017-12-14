#!/usr/bin/python3

from socket import *
import threading
import sys
import locale, datetime
import time
import os

DEFAULT_PORT = 10000

def readClient(serverSocket):
  try:  
    while True:
      rec_packet, addr = serverSocket.recvfrom(5120)
  except:
    serverSocket.close()
              
def main(serverPort):
  serverSocket = socket(AF_INET, SOCK_RAW, IPPROTO_ICMP)
  serverSocket.bind(('localhost',serverPort))
  serverSocket.setsockopt(SOL_IP, IP_HDRINCL, 1)
  print('Ready to serve on port',serverPort)
  
  try:
      workerThread = threading.Thread(target = readClient, args=(serverSocket,))
      #workerThread2 = threading.Thread(target = sendClient, args=(connectionSocket,)) 
      workerThread.start()
      #workerThread2.start()
  
  except KeyboardInterrupt:
    connectionSocket.send("Server shutting down now! Thanks for pinging!\n".encode())
    serverSocket.close()
    workerThread.join()
    print("Shutdown complete... exiting")
    sys.exit()
                  
if __name__ == "__main__":
  servPort = DEFAULT_PORT
  main(servPort)

