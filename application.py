from flask import Flask
from flask_socketio import SocketIO, emit

# Create flask and socketio objects
app = Flask(__name__)
socketio = SocketIO(app)

# Print message when client connects
@socketio.on('connect')
def user_has_connected():
    print('a user connected to a group')
    emit('aUserHasConnectedToAGroup', broadcast=True)

# Print message when client disconnects
@socketio.on('disconnect')
def user_has_disconnected():
    print('a user disconnected to a group')
    emit('aUserHasDisconnectedToAGroup', broadcast=True)

@socketio.on('clientPhotoUploaded')
def broadcast_image_uploaded():
    print('received client message')
    emit("imageUploadedToGroupName", broadcast=True)

# Run gevent web server
if __name__ == '__main__':
    socketio.run(app)
