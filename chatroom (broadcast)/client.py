from socket import *
import threading
host="127.0.0.1"
port=2177

client_socket=socket(AF_INET, SOCK_STREAM)
client_socket.connect((host, port))
def recv_msg():
    while True:
        recv_data=client_socket.recv(2048).decode("utf=8")
        print(recv_data)
thread=threading.Thread(target=recv_msg)
thread.start()

while True:
    send_data=input("")
    client_socket.send(send_data.encode("utf-8"))
    client_socket.close()