# Task 13: Implement Notifications in Flask App using WebSockets

#pip install Flask-SocketIO eventlet

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


import time

@app.route('/trigger_notification')
def trigger_notification():
    # Simulate an event that triggers a notification
    notification_data = {
        'message': 'New notification message',
        'timestamp': time.strftime('%Y-%m-%d %H:%M:%S')
    }
    # Send the notification to all connected clients
    socketio.emit('notification', notification_data)
    return 'Notification triggered!'


if __name__ == '__main__':
    socketio.run(app)

