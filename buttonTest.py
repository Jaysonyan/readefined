import RPi.GPIO as GPIO
from picamera import PiCamera
import time
import os
from PIL import Image

sizeX = 1000
sizeY = 1000

def record():
    camera = PiCamera()
    camera.iso = 800
    #camera.zoom = (0.25, 0.25, 0.5, 0.5)
    camera.start_preview()
    while True:
	time.sleep(2)
        camera.capture("image.jpg")
        img = Image.open("image.jpg")
        img = img.crop(sizeX/4,sizeY/4,sizeX*3/4,sizeY*3/4)
        crop.save("image.jpg")
        os.system("python master.py")
	input_state = GPIO.input(18)
        if input_state == False:
            break
    camera.stop_preview()

GPIO.setmode(GPIO.BCM)
GPIO.setwarnings(False)
GPIO.setup(18, GPIO.IN, pull_up_down = GPIO.PUD_UP)
GPIO.setup(23, GPIO.OUT)
GPIO.output(23, GPIO.LOW)
while True:
           input_state = GPIO.input(18)
           if input_state == False:
               GPIO.output(23, GPIO.HIGH)
               print("Button Pressed")
               record()
               break
               
GPIO.cleanup()


