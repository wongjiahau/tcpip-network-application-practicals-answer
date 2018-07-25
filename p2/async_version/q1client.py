import rpyc


def show_result(x):
    print(f"The result is {x.value}")

proxy = rpyc.connect("localhost", port=8080)


async_calculateVolt = rpyc.async_(proxy.root.calculateVolt)

current = float(input("Enter current: "))
resistance = float(input("Enter resistance: "))

promise = async_calculateVolt(current, resistance)
promise.add_callback(show_result)
promise.wait()

