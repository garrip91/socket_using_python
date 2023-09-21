import socket


new_socket = socket.socket()
new_socket.bind(("127.0.0.1", 1500))
new_socket.listen()

print("Сервер запущен!")
name = input("Введите своё имя:\n")
conn, add = new_socket.accept()

client = (conn.recv(1024)).decode()
print(f"{client} присоединился!")
conn.send(name.encode())

while True:
    message = input("Я: ")
    conn.send(message.encode())
    message = conn.recv(1024)
    message = message.decode()
    print(f"{client}: {message}")
