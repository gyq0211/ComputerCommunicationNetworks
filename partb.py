import socket


serverSocket = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
serverPort = 6789
serverSocket.bind(("", serverPort))
serverSocket.listen(1)

while True:
    
    print('The server is ready to receive')
    connectionSocket, addr = serverSocket.accept()
    
    try:
        message = connectionSocket.recv(1024).decode()
        filename = message.split()[1]
        filename = filename[1:]
        print(filename)
        print('this is file name:'+filename)

        if filename == '':
            f = open('helloworld.html')
            outputdata = f.read()
            connectionSocket.send("HTTP/1.1 200 OK\r\n\r\n".encode())
            for i in range(0, len(outputdata)):
                connectionSocket.send(outputdata[i].encode())
            connectionSocket.send("\r\n".encode())

        if 'red' in filename:
            f = open('helloworld2.html')
            outputdata = f.read()
            connectionSocket.send("HTTP/1.1 200 OK\r\n\r\n".encode())
            for i in range(0, len(outputdata)):
                connectionSocket.send(outputdata[i].encode())
            connectionSocket.send("\r\n".encode())

        if 'green' in filename:
            f = open('helloworld3.html')
            outputdata = f.read()
            connectionSocket.send("HTTP/1.1 200 OK\r\n\r\n".encode())
            for i in range(0, len(outputdata)):
                connectionSocket.send(outputdata[i].encode())
            connectionSocket.send("\r\n".encode())

        if filename != '' and 'red' not in filename and 'green' not in filename:
            connectionSocket.send("HTTP/1.1 404 Not Found\r\n\r\n".encode())
            connectionSocket.send(
                "<html><head></head><body><h1>404 Not Found</h1></body></html>\r\n".encode())

        connectionSocket.close()

    except IOError:
        connectionSocket.send("HTTP/1.1 404 Not Found\r\n\r\n".encode())
        connectionSocket.send("<html><head></head><body><h1>404 Not Found</h1></body></html>\r\n".encode())
        connectionSocket.close()

serverSocket.close()
sys.exit()

