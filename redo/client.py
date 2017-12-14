#!/usr/bin/python3
import sys
from socket import *
import threading

def readFromServer(cS):
  while True:
    try:
      recvMessage = cS.recv(1024).decode()
      print(recvMessage)
    except OSError:
      break

def main():
  serverName = ''
  serverPort = 10000
  threads = []
  cS = socket(AF_INET, SOCK_STREAM)
  print("Socket created") 
  cS.connect((serverName, serverPort))
  print("Connection achieved")
  #cS.send('hello, this is the client'.encode())
  
  workerThread = threading.Thread(target = readFromServer, args=(cS,))
  workerThread.start()
  data = "This is the hard-coded thesage"
  #chk = checksum(data)

  msg_type = '\x08' # ICMP Echo Request
  msg_code = '\x00' # must be zero
  msg_checksum_padding = '\x00\x00' # "...with value 0 substituted for this field..."
  rest_header = '\x00\x01\x00\x01' # from pcap
  entire_message = msg_type + msg_code + msg_checksum_padding + rest_header + data
  entire_chk = entire_message
  #entire_chk = checksum(entire_message)
  header = "Type: 8(require)or0(reply)\r\nChecksum: " + str(entire_chk) + "\r\nIdentifier (BE): XXX\r\nIdentifier (LE): XXX\r\nSequence number (BE): XXX\r\nSequence number (LE): XXX\r\n"
  icmpPack = header + "Data: " + data + "\r\n\r\n"
  cS.send(icmpPack.encode())
  cS.close()
  workerThread.join()
  sys.exit()

if __name__ == '__main__':
  main()


