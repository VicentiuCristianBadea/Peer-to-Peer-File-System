import socket
import sys
import struct
import json

#  ------------------------UDP-------------------------------
#                   SERVER COMMUNICATION
#  ----------------------------------------------------------
client_host = '0.0.0.0'
client_port = 8893

# port needs to be the same as server port
server_port = 8892
# Using client IP Address
server_host = 'localhost'

try:
    s = socket.socket(socket.AF_INET, socket.SOCK_DGRAM)
except socket.error:
    print('Failed to create socket')
    sys.exit()

s.bind((client_host, client_port))

while True:
    msg = "REGISTER"
    msg_format = {"header": msg}
    msg_json = json.dumps(msg_format)

    try:
        s.sendto(msg_json, (server_host, server_port))

        data = s.recvfrom(1024)
        reply = data[0]
        addr = data[1]

        print('Server reply : ' + reply)


    except socket.error as msg:
        print('Error')
