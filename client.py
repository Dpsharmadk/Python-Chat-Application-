import socket

HOST = "127.0.0.1"
PORT = 5000

client = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
client.connect((HOST, PORT))

print("Connected to server.")

while True:
    msg = input("Client: ")
    client.send(msg.encode())

    server_msg = client.recv(1024).decode()

    if not server_msg:
        break

    print(f"Server: {server_msg}")

client.close()