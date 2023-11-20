# Task 11: Create a Real-time Chat Application using Flask-SocketIO

pip install Flask-SocketIO eventlet

from flask import Flask, render_template
from flask_socketio import SocketIO

app = Flask(__name__)
socketio = SocketIO(app)

@app.route('/')
def index():
    return render_template('index.html')

@socketio.on('message')
def handle_message(message):
    socketio.emit('message', message)

if __name__ == '__main__':
    socketio.run(app)
