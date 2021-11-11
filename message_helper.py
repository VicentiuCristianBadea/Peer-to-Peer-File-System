import registration_message
import server

class MessageHelper():


    @staticmethod
    def checkMessageType(self, data):
        #   TODO: Check the message type
        
        #   Perhaps we can implement a factory pattern to 
        #   return appropriate solution

        print(data.strip())
        return


    def userRegisterRequest(self, user): 
        self.sendAcceptRegisterMessage(user) if server.reg_users.addUser(user)\
            else self.sendDenyRegisterMessage(user) 

    def sendAcceptRegisterMessage(self, user):
        #   TODO: Send accept registration message
        user.RQ = server.RQ
        rm = registration_message.userMessage(self.accept_msg_type) 
        self.sendMessageToUser()

    def sendDenyRegisterMessage():
        #   TODO: Send deny registration message
        return

    def sendMessageToUser(user, userMessage):
        #   TODO: Send a message to a user
        return