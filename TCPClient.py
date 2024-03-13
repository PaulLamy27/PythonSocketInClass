from socket import *
# name and port help to identify the server
serverName = "localhost"
serverPort = 12000

# TCP socket create
# AF_INET means using the internet 
# SOCK_STREAM means it uses TCP
clientSocket = socket(AF_INET, SOCK_STREAM)
clientSocket.connect((serverName,serverPort))

# prompt
sentence = input("Input lowercase sentence:")

# sends the sentence through the client’s socket and into the TCP connection
clientSocket.send(sentence.encode())

# chars that arrive are placed into modifiedSentence
# chars will accumulate until the lines ends with carriage char.
modifiedSentence = clientSocket.recv(1024)

print("From Server: ", modifiedSentence.decode()) 
clientSocket.close()