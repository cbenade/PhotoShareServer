# PhotoShareServer

## Tech Choice
PhotoShareServer was written in [Python](https://docs.python.org/3/) with [Flask](http://flask.palletsprojects.com/en/1.1.x/) and [SocketIO](https://flask-socketio.readthedocs.io/en/latest/) for their ease of use and the plentiful amount of support available for either framework/library on question and answer sites like [Stack Overflow](https://stackoverflow.com/).

## The WebSocket Protocol
SocketIO was chosen as the library to write PhotoShareServer for it's ability to connect users to the service using the WebSocket protocol. WebSockets/SocketIO enables the sending and recieving of information between a server and connected devices without a client first being required to send a "GET/POST" request any time they would like to recieve the most up-to-date information. Once a connection between the client and server has been sucessfully established, the server is able to freely send up-to-date information to the client as soon as it becomes available. 

## SocketIO Rooms
One of SocketIO's great features is it's ability to categorize related groups of users on a server through the functionality of "rooms". Joining users into rooms enables the server to emit messages to large pools of users with just a single emit command. 

This feature is utilized by PhotoShareServer as a mechanism through which users connected to the same photo feed can relay update notifications to eachother upon receiving a successful "image uploaded" status. This means that devices connected to the same room will be automatically prompted to download and receive the latest AWS images without requiring a manual page-refresh by the connected user.

## Heroku
[Heroku](https://www.heroku.com/) was chosen as the platform to host PhotoShareServer for it's ease of use and the countless number of online examples from past users regarding troubleshooting any potential issues. Heroku's built-in integration with [GitHub](https://github.com/) makes it easy to post application script updates and server dynos can be easily enabled/disabled by using the easy to learn Heroku CLI tool from any computer's terminal. 
