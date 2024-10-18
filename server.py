import socket
import threading

server_ip = '127.0.0.1'
server_port = 12345
buffer_size = 1024
clients = []

def broadcast(message, sender_address):
    for client in clients:
        if client != sender_address:
            server_socket.sendto(message, client)

def handle_client():
    while True:
        message, client_address = server_socket.recvfrom(buffer_size)
        if client_address not in clients:
            clients.append(client_address)
        broadcast(message, client_address)

server_socket = socket.socket(socket.AF_INET, socket.SOCK_DGRAM)
server_socket.bind((server_ip, server_port))

thread = threading.Thread(target=handle_client)
thread.start()

