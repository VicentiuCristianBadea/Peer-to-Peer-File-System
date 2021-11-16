import socket
import sys


 # ------------------------TCP-------------------------------
 #                  PEER COMMUNICATION - Acting Client Side
 # ----------------------------------------------------------

s = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
host = input(str("Please enter the host address of the sender"))
port = 8080
s.connect((host,port))
print("Connected..")

fileName = input(str("Please enter a filename for the incoming file: "))
file = open(fileName, 'wb')
fileData = s.recv(1024)
file.write(fileData)
file.close()
print("File has been received successfully")

