import socket
import json

HOST = ""
PORT = 8080

s = socket.socket(socket.AF_INET, socket.SOCK_STREAM)

s.bind((HOST, PORT))
s.listen()

conn, address = s.accept()

data = json.loads(conn.recv(1024).decode())

volt = float(data["current"]) * float(data["resistance"])

response = str(volt).encode()

conn.sendall(response)


