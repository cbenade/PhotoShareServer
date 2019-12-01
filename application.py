from flask import Flask
from flask_socketio import SocketIO, emit

# Create flask and socketio objects
app = Flask(__name__)
socketio = SocketIO(app)

# Print message when client connects
@socketio.on('connect')
def user_has_connected():
    print('a user connected')
    userHasConnected()
def userHasConnected():
    emit('aUserHasConnected', broadcast=True)

# Print message when client disconnects
@socketio.on('disconnect')
def user_has_disconnected():
    print('a user disconnected')
    userHasDisconnected()
def userHasDisconnected():
    emit('aUserHasDisconnected', broadcast=True)

@socketio.on('uploadNotification')
def notified_image_uploaded():
    print('received client notification')
    broadcast_image_uploaded()
def broadcast_image_uploaded():
    emit("imageUploaded", broadcast=True)

# Run gevent web server
if __name__ == '__main__':
    socketio.run(app)
