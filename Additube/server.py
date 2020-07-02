import socket

TCP_IP = '127.0.0.1'
TCP_PORT = 135
BUFFER_SIZE = 20  # Normally 1024, but we want fast response

s = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
#s.bind((TCP_IP,TCP_PORT))
s.bind(('localhost', 80))
s.listen(5)

#conn, addr = s.accept()
#print("Connection address: ", addr)
##print 'Connection address:', addr

#while 1:
    #data = conn.recv(BUFFER_SIZE)
    #if not data: break
    #print("recived data: ", data)
    #conn.send(data)  # echo
#conn.close()



while True:
    # accept connections from outside
    (clientsocket, address) = s.accept()
    print("Connection address: ", address)
    # now do something with the clientsocket
    # in this case, we'll pretend this is a threaded server
    ct = client_thread(clientsocket)
    ct.run()
