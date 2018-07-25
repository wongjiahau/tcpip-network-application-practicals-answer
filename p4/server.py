from flask import Flask
from flask_socketio import SocketIO, emit
import json

total = 0
app = Flask(__name__)
app.config['SECRET_KEY'] = 'secret!'
socketio = SocketIO(app)

@socketio.on("connect", namespace="/customer-census")
def handle_connect():
    global total
    broadcast_total_customers(total)
    print("connected")

@socketio.on("client_connected", namespace="/customer-census")
def handle_client_connected(data):
    print(data)

@socketio.on("update_sent", namespace="/customer-census")
def handle_update_sent(data):
    global total
    total += data["numberOfCustomers"]
    broadcast_total_customers(total)

def broadcast_total_customers(n):
    emit("broadcast_update", json.dumps({"totalCustomers": n}), broadcast=True, namespace="/customer-census")

socketio.run(app)