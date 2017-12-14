from socket import *
import os as os
from time import gmtime, strftime


serverPort = ???

serverSocket = socket(AF_INET, SOCK_STREAM)
serverSocket.bind(('', serverPort))
serverSocket.listen(1)

def sebdICMP():
  checkSum = getChecksum()
  packet = "Type: 8(require)or0(reply)\r\nChecksum: " + checkSum + "\r\nIdentifier (BE): XXX\r\nIdentifier (LE): XXX\r\nSequence number (BE): XXX\r\nSequence number (LE): XXX\r\n\r\n"
