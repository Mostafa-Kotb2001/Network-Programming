from socket import *
import threading
host="127.0.0.1"
port=2177
server_socket=socket(AF_INET,SOCK_STREAM)
server_socket.bind((host,port))
server_socket.listen()
clients=[]
def broadcast_msg(message, currentclient):
    for client in clients:
        if client!= currentclient:
            client.send(message.encode("utf-8"))
def recv_msg(client):
    while True:
        message=client.recv(2048).decode("utf=8")
        broadcast_msg(message,client)
 
while True:
    client_socket , client_addr = server_socket.accept()
    clients.append(client_socket)
    thread=threading.Thread(target=recv_msg ,args=clients)
    thread.start()
    server_socket.close()
