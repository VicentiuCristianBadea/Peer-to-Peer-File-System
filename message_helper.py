import registration_message
import server
import json
import DBHelper

class MessageHelper():
    
    def __init__():
        self.db_helper = DBHelper


    @staticmethod
    def checkMessageType(data):
        #   TODO: Check the message type
        
        #   Perhaps we can implement a factory pattern to 
        #   return appropriate solution

        json_data = json.loads(data)

        # REGISTER | NAME | RQ# | 

        
        print(str(json_data["header"]))

        # call DBHeler.REGISTER(Client)
        # returns tuple -> boolean, error
        return


    def userRegisterRequest(self, client): 
        self.sendAcceptRegisterMessage(client) if server.reg_users.addUser(client)\
            else self.sendDenyRegisterMessage(client) 

    def sendAcceptRegisterMessage(self, client):
        #   TODO: Send accept registration message
        #client.RQ = server.RQ
        rm = registration_message.userMessage(self.accept_msg_type) 
        self.sendMessageToUser()

    def sendDenyRegisterMessage():
        #   TODO: Send deny registration message
        return

    def sendMessageToUser(client, userMessage):
        #   TODO: Send a message to a client
        return


