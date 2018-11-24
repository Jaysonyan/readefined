import RPi.GPIO as GPIO
from picamera import PiCamera
import time


def record():
    camera = PiCamera()
    camera.iso = 800
    camera.zoom = (0.25, 0.25, 0.5, 0.5)
    camera.start_preview()
    while True:
        camera.capture("image.jpg")
        input_state = GPIO.input(18)
        if input_state == False:
            break
        time.sleep(0.1)
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
               
os.system("python master.py")
GPIO.cleanup()


