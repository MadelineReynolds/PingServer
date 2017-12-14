#!/usr/bin/python3
import sys
import base64
import hashlib
from socket import *
import threading

def carry_around_add(a, b):
  c = a + b
  return (c & 0xffff) + (c >> 16)

def calculateCheckSum(message):
  length = len(message)
  if(length%2 != 0):
    message = message + '\x00'
  #https://wiki.python.org/moin/BitwiseOperators
  #bitString = byteArray(message)
  s = 0
  for i in range(0, len(message), 2):
    w = ord(message[i]) + (ord(message[i+1]) << 8)
    s = carry_around_add(s, w)
  return ~s & 0xffff

def pingServer(csock, message):
  try:
    data = message
    pingType = '\x08' 
    pingCode = '\x00' 
    pingCheckPad = '\x00\x00' 
    pingRestHead = '\x00\x01\x00\x01' 
    entireMessage = pingType + pingCode + pingCheckPad + pingRestHead + data
    chk = calculateCheckSum(entireMessage)
    #chk = hex(chk)
    print(chk)
    entireMessage = pingType + pingCode + chk + pingRestHead + data
    csock.send(entireMessage.encode())
    csock.close()
  except:
    csock.close()

def main():
  serverName = ''
  serverPort = 10000
  threads = []
  clientSocket = socket(AF_INET, SOCK_RAW, IPPROTO_ICMP)
  print("Socket created") 
  clientSocket.connect((serverName, serverPort))
  print("Connection achieved")
  message = input('Enter your secret message: ')
  message = (base64.encodestring(message.encode())).decode()
  #https://code.tutsplus.com/tutorials/base64-encoding-and-decoding-using-python--cms-25588
  workerThread = threading.Thread(target = pingServer, args=(clientSocket,
    message))
  workerThread.start()
  
  try:
    while (1):
      message = clientSocket.recv(1024)
      message = message.decode()
      print(message)
      if len(message) == 0: 
        raise Exception("Client closed unexpectedly")
  
  except:
    clientSocket.close()
  
  clientSocket.close()
  workerThread.join()
  sys.exit()

if __name__ == '__main__':
  main()


