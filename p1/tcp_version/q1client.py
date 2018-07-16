import socket
import json

current = float(input("Enter current : "))
resistance = float(input("Enter resistance : "))

request = json.dumps({
    "current": current,
    "resistance": resistance
})

s = socket.socket(socket.AF_INET, socket.SOCK_STREAM)

conn = s.connect(("", 8080))

s.sendall(request.encode())

response = s.recv(1024).decode()

print(f"The resistance is {response}")
