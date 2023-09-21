import socket


socket_server = socket.socket()

name = input("Введите своё имя:\n")
socket_server.connect(("127.0.0.1", 1500))
socket_server.send(name.encode())
socket_name = socket_server.recv(1024)
server_name = socket_name.decode()
print(f"{server_name} присоединился!")

while True:
    message = (socket_server.recv(1024)).decode()
    print(f"{server_name}: {message}")
    message = input("Я:\n")
    socket_server.send(message.encode())
