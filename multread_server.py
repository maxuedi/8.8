import threading
import socket
# from threading import Thread

HOST = '0.0.0.0'   # Symbolic name meaning all available interfaces
PORT = 8000 # Arbitrary non-privileged port

s = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
print ('Socket created')

#Bind socket to local host and port

s.bind((HOST, PORT))

print ('Socket bind complete')

#Start listening on socket
s.listen(10)
print ('Socket now listening')

#Function for handling connections. This will be used to create threads
def clientthread(conn):
    #Sending message to connected client
    data = 'Welcome to the server.'
    data2='Connected with ' + addr[0] + ':' + str(addr[1])+'  '
    data1 = data2+data
    conn.send(data1.encode()) #send only takes string

    #infinite loop so that function do not terminate and thread do not end.
    while True:

        #Receiving from client
        data = conn.recv(1024)
        reply =  data
        if not data: 
            break

        conn.sendall(reply)

    #came out of loop
    conn.close()

#now keep talking with the client
while 1:
    #wait to accept a connection - blocking call
    conn, addr = s.accept()
    data2='Connected with ' + addr[0] + ':' + str(addr[1])
    print (data2)

    #start new thread takes 1st argument as a function name to be run, second is the tuple of arguments to the function.
    
    
    t1=threading.Thread(target=clientthread ,args=(conn,))
    t1.start()

s.close()
