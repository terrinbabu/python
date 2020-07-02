import socket
import random

host = '127.0.0.1'
port = 5000
s = socket.socket()
s.connect((host,port))
BUFFER_SIZE = 1024

message = input("-> ")

while message != 'q':
  s.send(message.encode())
  data = s.recv(1024)
  print("recived data from server:", data)
  message = input("-> ")
  
##while True:
    
    ##message = random.randint(0,360)
    ##message_str = str(message)
    ##print(message_str)
    ##s.send(message_str.encode())
    
    ##data = s.recv(BUFFER_SIZE)
    ##print("recived data: ", data)
    
    ##if 0xFF == ord('c'):
        ##break


##TCP_IP = '127.0.0.1'
##TCP_PORT = 135
##BUFFER_SIZE = 1024
##MESSAGE = "Hello, World!"
##s = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
##s.connect((TCP_IP, TCP_PORT))
###s.send(MESSAGE)
##s.sendall(MESSAGE.encode())
##data = s.recv(BUFFER_SIZE)
##print("recived data: ", data)
##s.close()
