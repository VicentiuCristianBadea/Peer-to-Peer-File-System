import users
import registration_message


class RegisteredUsers():
    def __init__(self):
        self.users = []
        self.usernames = []

    #   Check if name exists, otherwise add them
    def addUser(self, user):
        return self.acceptUser(user) \
            if self.checkUser(user) else self.denyUser()

    #   Remove the username and user from the lists
    def removeUser(self, user):
        users.remove(user)
        self.usernames.remove(user.name)
    
    #   Check if name is in usernames
    def checkUser(self, user):
        return user.name in self.usernames

    #   
    def denyUser():
        return False

    #   Append user to lists and return true
    def acceptUser(self, user):
        self.users.append(user)
        self.usernames.append(user.name)
        return True

        
