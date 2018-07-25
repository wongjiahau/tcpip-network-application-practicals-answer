import rpyc
from rpyc.utils.server import ThreadedServer

class MyService(rpyc.Service):
    def exposed_calculateVolt(self, current, resistance):
        return current * resistance

    def on_connect(self, conn):
        print(f"Connected at {conn}")

    def on_disconnect(self, conn):
        print(f"Disconnected at {conn}")

t = ThreadedServer(MyService, port=8080)
t.start()
