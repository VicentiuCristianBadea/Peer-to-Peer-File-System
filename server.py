import registered_users
import registration_message
import users
import socket
import threading
import sys


class UDP_server(threading.Thread):
    def __init__(self, host, port):
        super(UDP_server, self).__init__()
        self.HOST = host
        self.PORT = port
        self.sleep_time = 3
        self.reg_users = registered_users.RegisteredUsers()
        self.accept_msg_type = "REGISTERED"
        self.deny_msg_type = "REGISTER-DENIED"
        self.RQ = 0
        self.s = socket
    def run(self):
        self.initServer()
        self.listening()

    def initServer(self):
        self.createSocket()
        self.bindSocket()
        
    def listening(self):
        while 1:
            d = self.s.recvfrom(1024)
            data = d[0]
            addr = d[1]

            if not data:
                break

            self.checkMessageType(d[0])


    def checkMessageType(self, data):
        #   TODO: Check the message type
        
        #           Perhaps we can implement a factory pattern to 
        #           return appropriate solution
        return


    def userRegisterRequest(self, user):
        self.sendAcceptRegisterMessage(user) if self.reg_users.addUser(user)\
            else self.sendDenyRegisterMessage(user) 

    def sendAcceptRegisterMessage(self, user):
        #   TODO: Send accept registration message
        user.RQ = self.RQ
        self.RQ += 1
        rm = registration_message.userMessage(self.accept_msg_type, self.RQ) 
        self.sendMessageToUser()

    def sendDenyRegisterMessage():
        #   TODO: Send deny registration message
        return

    def sendMessageToUser(user, userMessage):
        #   TODO: Send a message to a user
        return


    def createSocket(self):
        try:
            self.s = socket.socket(socket.AF_INET, socket.SOCK_DGRAM)
            print('Socket Created')
        except socket.error as msg:
            print ('Failed to create socket. Error Code: ') + \
                str(msg[0])\
                + ' Message ' + msg[1]
            sys.exit()

    def bindSocket(self):
        try:
            self.s.bind((self.HOST, self.PORT))
        except socket.error as msg:
            print ('Bind failed. Error Code: ') + str(msg[0])\
                 + ' Message ' + msg[1]
            sys.exit()

        print ('Socket bind complete')
