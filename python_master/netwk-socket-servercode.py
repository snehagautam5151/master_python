import socket
try:
    print("craete an INET,STREAMing socket")
    serverSocket = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
    print("bind the socket to a public host.and a well-know port 8080")
    serverSocket.bind((socket.gethostname(),8080))
    print("become a server socket")
    serverSocket.listen(5)
    while True:
        print("accept the connection from outside")
        (clientSocket,address) = serverSocket.accept()
except Exception as e:
        print(e)