import server


host = '0.0.0.0'
port = 8892

serverThread = server.UDP_server(host, port)
serverThread.start()


serverThread.join()