from socket import *
# port identifies server
serverPort = 12000

# TCP socket create
# AF_INET means using the internet 
# SOCK_STREAM means it uses TCP
serverSocket = socket(AF_INET,SOCK_STREAM)

# associate server port number with the socket
serverSocket.bind(("",serverPort))

# serverSocket is welcoming socket. wait until a client 'knocks on the door'
# and arrives at the socket 
serverSocket.listen(1)

print("The server is ready to receive")

# waiting for the client to request
while True:
    # accept is for TCP, but not for UDP
    connectionSocket, addr = serverSocket.accept()
    # creates another socket
    sentence = connectionSocket.recv(1024).decode()
    capitalizedSentence = sentence.upper()
    connectionSocket.send(capitalizedSentence.encode()) 
    connectionSocket.close()