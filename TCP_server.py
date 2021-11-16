import socket
import sys
import struct
import json


# ------------------------TCP-------------------------------
#                  PEER COMMUNICATION - Acting Server Side
# ----------------------------------------------------------


def createSocket():
    try:
        global s
        global host
        global port

        s = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
        host = socket.gethostname()
        print(host)
        port = 8080
        print("Socket Created.")

    except socket.error as msg:
        print("Socket creation error: " + str(msg))


# Binding the Socket and listening for connections
def bindSocket():
    try:
        global host
        global port
        global s

        print("Binding the port: " + str(port))

        # bind socket
        s.bind((host, port))

        # listen for connections (max 1 bad connections before throwing error)
        # only listen in TCP.
        s.listen(1)

    except socket.error as msg:
        print("Socket binding error: " + str(msg) + "\n" + "Retrying....")
        bindSocket()


# Establish connections with another Client (Socket must be listening)
def accepting_connection():
    while True:
        try:
            conn, address = s.accept()

            # Prevent timeout from happening
            s.setblocking(1)

            print("Connection has been established with IP: " + address[0] + " | Port : " + str(address[1]))

            # Put file transfer function here.
            sendFile(conn)
            conn.close()

        except:
            print("Error accepting connections")


def sendFile(conn):
    fileName = input(str("Please Enter the File Name Of the File you want"))
    file = open(fileName, 'rb')
    fileData = file.read(200)
    conn.send(fileData)
    print("Data Has been transmitted Successfully")


createSocket()
bindSocket()
accepting_connection()