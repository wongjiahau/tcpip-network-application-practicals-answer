from rpyc.utils.server import ThreadedServer
import rpyc

class MyService(rpyc.Service):
    def exposed_calculateVolt(self, current, resistance):
        return current * resistance

t = ThreadedServer(MyService, port=8080)
t.start()


