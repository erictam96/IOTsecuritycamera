from grovepi import *
import os

ultrasonic_ranger = 15
relay_pin = 5

pinMode(relay_pin,"OUTPUT")
pinMode(ultrasonic_ranger,"INPUT")

while True:
    try:
        distant = ultrasonicRead(ultrasonic_ranger)
        print(distant,'cm')
        if distant <= 10:
            digitalWrite(relay_pin,1)
            os.system('python3 main.py')
        else:
            digitalWrite(relay_pin,0)
    except TypeError:
        print("TypeError")
    except IOError:
        print("IOError")