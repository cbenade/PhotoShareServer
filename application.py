from os import environ
from flask import Flask, render_template
from flask_socketio import SocketIO, send, emit, Namespace
from time import sleep

# Create flask and socketio objects
app = Flask(__name__)
app.config['SECRET_KEY'] = 'secret!'
socketio = SocketIO(app)

# Print message when client connects
@socketio.on('connect')
def user_has_connected():
    print('a user connected')
    emit('response1')

# Print message when client disconnects
@socketio.on('disconnect')
def user_has_disconnected():
    print('a user disconnected')
    emit('response2')

# Run gevent web server
if __name__ == '__main__':
    # socketio.run(app)
    socketio.run(environ.get('PORT'))
