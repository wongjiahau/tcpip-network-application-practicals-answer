import socket
import json

s = socket.socket(socket.AF_INET, socket.SOCK_STREAM)

s.connect(("", 8080))

x1 = float(input("x1 : "))
x2 = float(input("x2 : "))
y1 = float(input("y1 : "))
y2 = float(input("y2 : "))

request = {
    "p1": { "x": x1, "y": y1 },
    "p2": { "x": x2, "y": y2 },
}

s.sendall(json.dumps(request).encode())

data = s.recv(1024).decode()

