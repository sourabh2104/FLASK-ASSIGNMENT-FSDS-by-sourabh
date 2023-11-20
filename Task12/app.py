# Task 12: Build a Flask App with Real-time Data Updates using WebSockets

pip install Flask-SocketIO eventlet

from flask import Flask, render_template
from flask_socketio import SocketIO

app = Flask(__name__)
socketio = SocketIO(app)

@app.route('/')
def index():
    return render_template('index.html')

@socketio.on('connect')
def handle_connect():
    print('Client connected')

@socketio.on('disconnect')
def handle_disconnect():
    print('Client disconnected')

@socketio.on('update_data')
def handle_update_data(data):
    # Handle the updated data (data received from the client)
    # Perform necessary operations with the data
    # Emit the updated data to all connected clients
    socketio.emit('data_updated', data)

if __name__ == '__main__':
    socketio.run(app)
