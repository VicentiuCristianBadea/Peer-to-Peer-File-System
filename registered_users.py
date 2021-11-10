import "users.py"
import "registration_message.py"


class RegisteredUsers():
    def __init__(self):
        self.users = []
        self.usernames = []

    #   Check if name exists, otherwise add them
    def addUser(User user):
        return acceptUser(user) \
            if checkUser(user) else denyUser()

    #   Remove the username and user from the lists
    def removeUser(User user):
        users.remove(user)
        usernames.remove(user.name)
    
    #   Check if name is in usernames
    def checkUser(User user):
        return user.name in self.usernames

    #   
    def denyUser():
        return false


    #   Append user to lists and return true
    def acceptUser(User user):
        self.users.append(user)
        self.usernames.append(user.name)
        return true

        
