#!/usr/bin/python3
import sys
from socket import *
import threading

def pingServer(csock):
  try:
    data = "This is the hard-coded thesage"
    #chk = checksum(data)
    msg_type = '\x08' # ICMP Echo Request
    msg_code = '\x00' # must be zero
    msg_checksum_padding = '\x00\x00' 
    rest_header = '\x00\x01\x00\x01' 
    entire_message = msg_type + msg_code + msg_checksum_padding + rest_header + data
    entire_chk = '0xff6c'
    header = "Type: 8\r\nCode: 0\r\nChecksum: " + str(entire_chk) + "\r\nIdentifier (BE): 19\r\nIdentifier (LE): 19\r\nSequence number (BE): 1\r\nSequence number (LE): 256\r\n"
    icmpPack = header + "Data: " + data + "\r\n\r\n"
    print(icmpPack)
    csock.send(icmpPack.encode())
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
  workerThread = threading.Thread(target = pingServer, args=(clientSocket,))
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


