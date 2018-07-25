import rpyc

proxy = rpyc.connect(host="localhost", port=8080)

current = float(input("Enter current: "))
resistance = float(input("Enter resistance: "))

volt = proxy.root.calculateVolt(12,34)

print(volt)
