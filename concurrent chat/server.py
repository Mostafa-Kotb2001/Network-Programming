import socket
import threading


def receive_messages(client):
    while True:
        try:
            size_bytes = client.recv(2048)
            data = client.decode('utf-8')
            print(data)
        except socket.error:
            break

def send_message(client):
    while True:
        data = input('Server :')
        client.send(data.encode('utf-8'))


def start_server():
    host = 'localhost'
    port = 8000

    server_socket = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
    server_socket.bind((host, port))
    server_socket.listen(5)
    print(f"Server started on {host}:{port}")
    while True:
        client_session, client_address = server_socket.accept()
        clients.append((client_session, client_address))
        print(f"Connected with {client_address}")
        receive_thread = threading.Thread(target=receive_messages, args=(client_session,))
        receive_thread.start()

        send_thread = threading.Thread(target=send_message, args=(client_session,))
        send_thread.start()


if __name__ == '__main__':
    clients = []
    start_server()