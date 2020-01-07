# PhotoShareServer

## Description
PhotoShareServer is a complimentary service meant to improve the experience of users using the PhotoShareApp. While the service is running, users are able to receive real-time updates/notifications 
regarding other users activities and gain the abilty to automatically refresh image data without the user needing to manually send "GET/POST" requests to the AWS service.

## How to Use
Nothing is required of the user in order to take advantage of PhotoShareServer's features. As long as the server is running, users will automatically make benefit of PhotoShareServer while continuing to use the client-side PhotoShareApp. 

## How it Works
PhotoShareServer's "application.py" works by using both [Flask](http://flask.palletsprojects.com/en/1.1.x/) and [SocketIO's](https://flask-socketio.readthedocs.io/en/latest/) open-source resources to create a simple web server capable of connecting users to the service and can relay messages regarding user activities to and from connected devices. The script itself is hosted and run on the [Heroku](https://www.heroku.com/) cloud application platform. 

PhotoShareApp can still function properly while PhotoShareServer is not running, but at the cost of a diminished user experience regarding real-time updates. 

## Useful CLI Commands
### AWS
* Empty AWS Bucket: aws s3 rm s3://photosharebucketcs50 --recursive

### Heroku
* Scale-up Heroku Service: heroku ps:scale web=1 -a photoshareserver
* Scale-down Heroku Service: heroku ps:scale web=0 -a photoshareserver
* Tail Server Logs: heroku logs --tail -a photoshareserver 
