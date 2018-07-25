import rpyc
import json
import sys

points = json.dumps({
    "x1": float(sys.argv[1]),
    "y1": float(sys.argv[2]),
    "x2": float(sys.argv[3]),
    "y2": float(sys.argv[4]),
})

proxy = rpyc.connect(host="localhost", port=8080, config={"allow_public_attrs": True})

async_calcm = rpyc.async_(proxy.root.calculateMidpoint)

promise = async_calcm(points)
promise.add_callback(lambda x: print(x.value))
promise.wait()

