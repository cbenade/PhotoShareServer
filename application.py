from flask import Flask
from flask_socketio import SocketIO, emit, join_room, leave_room

# Create flask and socketio objects
app = Flask(__name__)
socketio = SocketIO(app)

# Print message when client connects
@socketio.on('connect')
def user_has_connected():
    print('a user connected')
    emit('aUserHasConnected', broadcast=True)

# Print message when client disconnects
@socketio.on('disconnect')
def user_has_disconnected():
    print('a user disconnected')
    emit('aUserHasDisconnected', broadcast=True)

# Place client in room
@socketio.on('join')
def on_join(room):
    print(f"user joined room '{room}'")
    join_room(room)

# Remove client from room
@socketio.on('leave')
def on_leave(room):
    print(f"user left room '{room}'")
    leave_room(room)

# Broadcast upload notification to devices connected in room
@socketio.on('uploadNotification')
def notified_image_uploaded(room):
    print('received client notification')
    emit("imageUploaded", room=room)

# Run eventlet web server
if __name__ == '__main__':
    socketio.run(app)
