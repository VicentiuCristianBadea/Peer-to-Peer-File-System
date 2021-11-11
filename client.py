import socket
import sys
import struct

# port needs to be the same as server port
PORT = 9999

#  Create TCP Socket
clientSocket = socket.socket(socket.AF_INET, socket.SOCK_STREAM)

# Using client IP Address
HOST = 'localhost'

# Create a tuple (Host IP Address, Port Number)
addr = (HOST, PORT)

# Connect using host/port number
# Binding socket
clientSocket.connect(addr)


while True:
    # buffer size of chunks (1024)
    msg = clientSocket.recv(1024)

#     check message for
