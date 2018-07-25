import socket

s = socket.socket(socket.AF_INET, socket.SOCK_DGRAM)
s.bind(("",8080))

data, addr = s.recvfrom(1024)

req = data.decode()

volt = float(req["current"]) * float(req["resistance"])

s.sendto(str(volt).encode(), addr)
