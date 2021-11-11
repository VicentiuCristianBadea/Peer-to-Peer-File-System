import threading
import sys
import message_helper


class ServerCheckMessage(threading.Thread):
    def __init__(self, msg):
        super(ServerCheckMessage, self).__init__()
        self.msg = msg
    def run(self):
        message_helper.checkMessageType(self.msg)
