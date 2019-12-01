from flask import Flask
from flask_socketio import SocketIO, emit, Namespace

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

@socketio.on('clientMessage')
def received_client_message(message):
    print('received client message: ' + message)
    response = message + "123"
    emit_server_message(response)
def emit_server_message(response):
    emit("serverMessage", response, broadcast=True)

# Run gevent web server
if __name__ == '__main__':
    socketio.run(app)
