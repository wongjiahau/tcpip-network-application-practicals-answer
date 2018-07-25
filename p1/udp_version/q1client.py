import socket
import json

current = float(input("Current : "))
resistance = float(input("Resistance : "))

request = json.dumps({
    "current": current,
    "resistance": resistance
}).encode()

s = socket.socket(socket.AF_INET, socket.SOCK_DGRAM)

s.sendto(request, ("",8080))

response, addr = s.recvfrom(1024)

print(response.decode())






