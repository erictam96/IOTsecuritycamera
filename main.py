import cv2
import sys
from mail import sendEmail
from flask import Flask, render_template, Response
from camera import VideoCamera
import time
import threading
import pyrebase
import datetime
import base64

now = datetime.datetime.now()

email_update_interval = 20 # sends an email only once in this time interval
video_camera = VideoCamera(flip=True) # creates a camera object, flip vertically
object_classifier = cv2.CascadeClassifier("models/facial_recognition_model.xml") # an opencv classifier

# App Globals (do not edit)
app = Flask(__name__)
last_epoch = 0



config = {
    "apiKey": "AIzaSyCh5gJt5Z94ZBVnM4iScsmPFNHgnf-Jhao",
    "authDomain": "smartsecurity-229ca.firebaseapp.com",
    "databaseURL": "https://smartsecurity-229ca.firebaseio.com",
    "storageBucket": "smartsecurity-229ca.appspot.com"
  }

firebase = pyrebase.initialize_app(config)
db = firebase.database()

def check_for_objects():
	global last_epoch
	while True:
		try:
			frame, found_obj = video_camera.get_object(object_classifier)
			if found_obj and (time.time() - last_epoch) > email_update_interval:
				last_epoch = time.time()
				print ('Sending email...')
				sendEmail(frame)
				d = now.strftime("%Y-%m-%d")
				t = now.strftime("%H:%M")
				img = base64.b64encode(frame)
				data = {'Date':d,'Time':t,'Image':str(img)}
				db.child('Security').push(data)
				print ('done!')
				
		except:
			print ('Error sending email: '), sys.exc_info()[0]

@app.route('/')
def index():
    return render_template('index.html')

def gen(camera):
    while True:
        frame = camera.get_frame()
        yield (b'--frame\r\n'
               b'Content-Type: image/jpeg\r\n\r\n' + frame + b'\r\n\r\n')


@app.route('/video_feed')
def video_feed():
    return Response(gen(video_camera),
                    mimetype='multipart/x-mixed-replace; boundary=frame')

if __name__ == '__main__':
    t = threading.Thread(target=check_for_objects, args=())
    t.daemon = True
    t.start()
    app.run(host='0.0.0.0', debug=False)
