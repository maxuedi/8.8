import socket
import time
i=0
while(i<100):
    client_sock=socket.socket(socket.AF_INET,socket.SOCK_STREAM)
    #建立连接
    address=("127.0.0.1",8000)
    client_sock.connect(address)
    #发送数据
    client_sock.send(b"hello")
    #接受数据
    data=client_sock.recv(1024)
    print(time.ctime())
    data = data.decode()
    print(f"接受到的数据为：{data}/n")
    #关闭连接
    i+=1
    client_sock.close()