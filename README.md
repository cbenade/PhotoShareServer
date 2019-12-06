# PhotoShareServer

## Description
PhotoShareServer is a complimentary service meant to improve the experience of users using the PhotoShareApp. While the service is running, users will be able to receive real-time updates/notifications 
regarding other users activities in the app and gain the abilty to refresh image data from the AWS service without the user needing to manually send "GET/POST" requests to the AWS service.

## How it works
PhotoShareServer's "application.py" works by using both [Flask](http://flask.palletsprojects.com/en/1.1.x/) and [SocketIO's](https://flask-socketio.readthedocs.io/en/latest/) open-source tools to create a simple web server capable of connecting users to the service and relay messages regarding user activities to and from connected devices. The script itself is hosted and run on the [Heroku](https://www.heroku.com/) cloud application platform. 

PhotoShareApp can still function properly while the PhotoShareServer is not running, but at the cost of a diminished user experience regarding real-time updates. 
