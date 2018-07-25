import socket
import json
import threading

class MyService(threading.Thread):
    def __init__(self, conn, addr):
        threading.Thread.__init__(self)
        self.conn = conn
        self.addr = addr
        print(f"Connected at {addr}")

    def run(self):
        request = self.conn.recv(1024).decode()
        data = json.loads(request)
        midpoint = {
            "x": (data["p1"]["x"] + data["p2"]["x"]) / 2,
            "y": (data["p1"]["y"] + data["p2"]["y"]) / 2,
        }
        self.conn.sendall(json.dumps(midpoint).encode())


s = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
s.bind(("", 8080))
s.listen()

while True:
    conn, addr = s.accept()
    MyService(conn, addr).start()
