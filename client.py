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
    msg_format = {"header":msg}
    msg_json = json.dumps(msg_format)

    try:
        s.sendto(msg_json, (server_host, server_port))

        data = s.recvfrom(1024)
        reply = data[0]
        addr = data[1]

        print('Server reply : ' + reply)
        

    except socket.error as msg:
        print('Error')
    



#  ------------------------TCP-------------------------------
#                   PEER COMMUNICATION
#  ----------------------------------------------------------
#
#
# def create_socket():
#     try:
#         global host
#         global port
#         global clientSocket
#         host = ""
#         port = 8080
#         clientSocket = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
#         print("Socket Created.")
#
#     except socket.error as msg:
#         print("Socket creation error: " + str(msg))
#
#
# # Binding the Socket and listening for connections
# def bind_socket():
#     try:
#         global host
#         global port
#         global clientSocket
#
#         print("Binding the port: " + str(port))
#
#         # bind socket
#         clientSocket.bind((host, port))
#
#         # listen for connections (max 5 bad connections before throwing error)
#         # only listen in TCP.
#         clientSocket.listen(5)
#
#     except socket.error as msg:
#         print("Socket binding error: " + str(msg) + "\n" + "Retrying....")
#         bind_socket()
#
#
# # Handling connection from multiple clients and saving to a list
# # Closing previous connections when server.py file is restarted
# def accepting_connections():
#     for c in all_connections:
#         c.close()
#
#     del all_connections[:]
#     del all_address[:]
#
#     while True:
#         try:
#             conn, address = s.accept()
#
#             # Prevent timeout from happening
#             s.setblocking(1)
#
#             all_connections.append(conn)
#             all_address.append(address)
#             print("Connection has been established : " + address[0])
#
#         except:
#             print("Error accepting connections")
#
#
# while True:
#     # buffer size of chunks (1024)
#     msg = clientSocket.recv(1024)
#
# #     check message for
