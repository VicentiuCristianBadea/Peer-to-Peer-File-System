class Client(dict):
    def __init__(self, name, ip, tcp_socket, files=None, udp_socket=None, RQ=None):
        super().__init__()
        if files is None:
            files = []
        self['RQ'] = RQ
        self['name'] = name
        self['ip'] = ip
        self['udp_socket'] = udp_socket
        self['tcp_socket'] = tcp_socket
        self['files'] = files

    def get_client_connection(self):
        my_dict = {'name': self['name'],
                   'ip': self['ip'],
                   'tcp_socket': self['tcp_socket']
                   }
        return my_dict

