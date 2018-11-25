import RPi.GPIO as GPIO
from picamera import PiCamera
from PIL import Image
import time
import os

imageStr = "image.jpg"


def record():
    camera = PiCamera()
    camera.iso = 800
    # camera.zoom = (0.25, 0.25, 0.5, 0.5)
    camera.start_preview()
    while True:
        #time.sleep(2)
        camera.capture(imageStr)
        img = Image.open(imageStr)
        sizeX = img.size[0]
        sizeY = img.size[1]
        img = img.crop((sizeX / 4, sizeY / 4, sizeX * 3 / 4, sizeY * 3 / 4))
	img = img.rotate(180)
        img.save(imageStr)
        os.system("python master.py")
        input_state = GPIO.input(26)
        if input_state == False:
            break
    camera.stop_preview()


GPIO.setmode(GPIO.BCM)
GPIO.setwarnings(False)
GPIO.setup(26, GPIO.IN, pull_up_down=GPIO.PUD_UP)
GPIO.setup(21, GPIO.OUT)
GPIO.output(21, GPIO.LOW)
while True:
    input_state = GPIO.input(26)
    if input_state == False:
        GPIO.output(21, GPIO.HIGH)
        print("Button Pressed")
        record()
        break

GPIO.cleanup()

