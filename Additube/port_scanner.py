import socket
import threading
from queue import Queue

sock = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
ip = '127.0.0.1'
server = 'www.gmail.com'

####  port scanner ####


#def pscan(port):
    #try:
        #sock.connect((ip,port))
        #return True
    #except:
        #return False

#for x in range(1,100):
    #if pscan(x):
        #print('Port ',x,' is open!!!!')
    #else:
        #print('Port ',x,' is closed')

#### threading port scanner ####

print_lock = threading.Lock()

def portscan(port):
    sock = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
    try:
        con = sock.connect((ip,port))
        with print_lock:
            print('Port ',port,' is open!!!!')
        con.close()
    except:
        pass
    
def threader():
    while True:
            worker = q.get()
            portscan(worker)
            q.task_done()

q = Queue()

for x in range(100):
    t = threading.Thread(target=threader)
    t.daemon = True
    t.start()
    
for worker in range(1,1000001):
    q.put(worker)

q.join()
