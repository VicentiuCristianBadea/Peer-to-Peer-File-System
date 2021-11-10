import server


host = '0.0.0.0'
port = 8888

serverThread = server.UDP_server(host, port)
serverThread.start()


serverThread.join()