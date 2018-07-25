import rpyc
import json
from rpyc.utils.server import ThreadedServer

class MyService(rpyc.Service):
    def exposed_calculateMidpoint(self, data):
        points = json.loads(data)
        return json.dumps({
            'x': (points['x1'] + points['x2']) / 2,
            'y': (points['y1'] + points['y2']) / 2
        })

t = ThreadedServer(MyService, port=8080)
t.start()
