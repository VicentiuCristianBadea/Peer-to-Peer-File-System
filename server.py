


class UDP_server(threading.Thread):
    def __init__(self, host, port):
        super(UDP_server, self).__init__()
        self.HOST = host
        self.PORT = port
        self.sleep_time = 3
        self.reg_users = RegisteredUsers()
        self.accept_msg_type = "REGISTERED"
        self.deny_msg_type = "REGISTER-DENIED"
        self.RQ = 0
    def run(self):
        initServer()
        listening()

    def initServer():
        createSocket()
        bindSocket()
        
    def listening():
        while 1:
            d = s.recvfrom(1024)
            data = d[0]
            addr = d[1]

            if not data:
                break

            checkMessageType(d[0])


    def checkMessageType(data):
        #   TODO: Check the message type
        
        #           Perhaps we can implement a factory pattern to 
        #           return appropriate solution


    def userRegisterRequest(User user):
        sendAcceptRegisterMessage(user) if reg_users.addUser(user)\
            else sendDenyRegisterMessage(user) 

    def sendAcceptRegisterMessage(User user):
        #   TODO: Send accept registration message
        user.RQ = RQ
        RQ += 1
        rm = userMessage(self.accept_msg_type,RQ) 
        sendMessageToUser()

    def sendDenyRegisterMessage():
        #   TODO: Send deny registration message

    def sendMessageToUser(User user, UserMessage userMessage):
        #   TODO: Send a message to a user


    def createSocket():
        try:
            s = socket.socket(socket.AF_INET, socket.SOCK_DGRAM)
            print 'Socket Created'
        except socket.error, msg:
            print 'Failed to create socket. Error Code: ' + \
                str(msg[0])\
                + ' Message ' + msg[1]
            sys.exit()

    def bindSocket():
        try:
            s.bind((self.HOST, self.PORT))
        except socket.error, msg:
            print 'Bind failed. Error Code: ' + str(msg[0])\
                 + ' Message ' + msg[1]
            sys.exit()

        print 'Socket bind complete'
