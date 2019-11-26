from flask import Flask, render_template
from flask_socketio import SocketIO, send, emit, Namespace

# Create flask and socketio objects
app = Flask(__name__)
socketio = SocketIO(app)

# Print message when client connects
@socketio.on('connect')
def user_has_connected():
    print('a user connected')
    userHasConnected()

# Print message when client disconnects
@socketio.on('disconnect')
def user_has_disconnected():
    print('a user disconnected')
    userHasDisconnected()

def userHasConnected():
    emit('event1', broadcast=True)

def userHasDisconnected():
    emit('event2', broadcast=True)

# Run gevent web server
if __name__ == '__main__':
    socketio.run(app)
