import rpyc
import json

proxy = rpyc.connect(host="localhost", port=8080)

x1 = float(input("x1: "))
y1 = float(input("y1: "))
x2 = float(input("x2: "))
y2 = float(input("y2: "))

points = json.dumps({
    'x1': x1,
    'y1': y1,
    'x2': x2,
    'y2': y2,
})

midpoint = json.loads(proxy.root.calculateMidpoint(points))

print(midpoint)
