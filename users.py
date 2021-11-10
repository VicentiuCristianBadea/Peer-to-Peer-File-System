#   User class describing each user in users list inside 
#   registered_users


class User():
    def __init__(self, RQ, name, ip, udp_socket, tcp_socket):
        self.RQ = rq
        self.name = name
        self.ip = ip
        self.udp_socket = udp_socket
        self.tcp_socket = tcp_socket