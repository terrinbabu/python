import socket # socket - open and close to aid communication between two entities
import random
import time
import random

sock = socket.socket(socket.AF_INET, socket.SOCK_STREAM)

#server = 'www.facebook.com'
#port = 80

#server_ip = socket.gethostbyname(server)

#request = "GET / HTTP/1.1\nHost: "+server+"\n\n"

#sock.connect((server,port))
#sock.send(request.encode())
#result = sock.recv(4096)

#print(result)

#ip = input(' Target IP: ')
#port = input(' Port : ')

ip = '127.0.0.1'
port = 135

sock.connect((ip,int(port)))

print("Socket connected to ", ip, "through port ", port)

while True:
    
    message = random.randint(1,23)
    message = str(message)

    sock.sendall(message.encode())
    print("message ", message, " sent successfully")

#reply = sock.recv(4096)
#print(reply.decode())


#bytes = random._urandom(1024)
#duration = input('Number of seconds to sent packets : ')
#timeout = time.time() + float(duration)
#sent = 0

#while True:
    #if time.time() > timeout:
        #break

    #sock.sendall(bytes,(ip,int(port)))
    #sent += 1
    #print("Send ", sent, "packet to ", ip, "through port ", port)
