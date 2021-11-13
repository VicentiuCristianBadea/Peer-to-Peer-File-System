class Client(dict):
    def __init__(self, name, ip, tcp_socket, udp_socket=None, files=None, RQ=None):
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

    def get_client_data(self):
        my_dict = self.get_client_connection()
        my_dict['files'] = self['files']
        return my_dict

    @classmethod
    def from_dict(cls, my_dict):
        params = ['name', 'ip', 'tcp_socket']
        if set(params).issubset(set(list(my_dict.keys()))):
            pass
        else:
            return None
