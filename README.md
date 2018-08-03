# Raspberry Pi Smart Security Camera integrated with Ultrasonic and Light sensor
In this project, we are implementing on the security camera integrated with ultrasonic and light sensor. The objective of this project is to capture an image when there is any motion is detected in the areas. Besides, ultrasonic is used to detect any obstacle with the effect range up to 4.5 meter, when there is any obstacle detected then the camera will be started to capture the motion. The reason to do this because ultrasonic draw lower current than camera, which mean it can achieve power saving.

## System Design
Hardware:
- Raspberry Pi 3 Model B
- Grove Pi
- Micro SD card
- Pi Camera Module V2
- Ultrasonic Sensor HC-SR04
- Grove Light Sensor 1.2
- LED Light Bulb

Software:
- Raspbian
- Python 3
- Firebase
- Gmail

## Functional/Modules Description
1. Image Capture by Motion Detection
    Pi will turn into a dedicated security camera that can monitor a connected camera to look for motion and periodically capture images. In addition, to detect the motion with the Pi camera, we use the motion software package provided from lavrsen.dk website.
    
2. Ultrasonic Object Range Detection
    The ultrasonic used to measure the distance to an object up to 4.5 meter by ultrasound. So, if there is an object come near, this module will start the Pi camera to capture the motion. The reason is ultrasonic draw lower current than camera and the camera do not require to 24 hour operating.
    
3. Light Sensor Detection
    The light sensor integrates a photo-resistor to detect the intensity of light. When the environment is dark, it will light up the LED bulb to provide sufficient light to the Pi camera (without IR) to capture a clear image.
    
4. Upload Image to Firebase Cloud
    Firstly, connect the Raspberry Pi with the Firebase through the Firebase API. When the security camera which using OpenCV has detecting a moving objects, it will automatically upload and store into Firebase Database. Thus, user can be easily view the images from the web browser or mobile devices.
    
5. Email Notification
    While the images have been uploaded to the Firebase, it will also use Gmail SMTP to send an email with images attached to user.
    
# Sample Screenshot

![alt text](https://s22.postimg.cc/vrf06m775/image.jpg) </br>
Figure 1: System built</br></br>
![alt text](https://s22.postimg.cc/bwsykif4x/image.jpg) </br>
Figure 2: User received email with images attached</br></br>
![alt text](https://s22.postimg.cc/6y5g5zqrl/image.jpg)</br>
Figure 3: Web browser to view all images from Database</br></br>
![alt text](https://s22.postimg.cc/f3ni44rv5/image.jpg)</br>
Figure 4: Firebase Database </br></br>
![alt text](https://s22.postimg.cc/68mntlvcx/image.jpg)</br>
Figure 5: Light sensor reading</br></br>
![alt text](https://s22.postimg.cc/4gtoypz5d/image.jpg)</br>
Figure 6: Ultrasonic distance reading</br>

