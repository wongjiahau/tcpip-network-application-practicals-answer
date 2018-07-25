import rpyc
from rpyc.utils.server import ThreadedServer
import json

class MyService(rpyc.Service):
    def exposed_calculateMidpoint(self, data):
        pts = json.loads(data)
        return json.dumps({
            "x": (pts["x1"] + pts["y1"]) / 2,
            "y": (pts["x2"] + pts["y2"]) / 2,
        })

t = ThreadedServer(MyService, port=8080)
t.start()





