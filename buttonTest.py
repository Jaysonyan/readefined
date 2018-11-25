import os
import time
import RPi.GPIO as GPIO
import threading
from picamera import PiCamera
from PIL import Image


imgStr = "image.jpg"

class callMasterThread (threading.Thread):
   def __init__(self, threadID, name, counter):
      threading.Thread.__init__(self)
      self.threadID = threadID
      self.name = name
      self.counter = counter
   def run(self):
      os.system("python master.py")

class flashLEDThread (threading.Thread):
   def __init__(self, threadID, name, counter):
      threading.Thread.__init__(self)
      self.threadID = threadID
      self.name = name
      self.counter = counter
   def run(self):
      ledOn = True
      while threading.activeThreads() > 1 :
          if ledOn:
              GPIO.output(20, GPIO.LOW)
          else:
              GPIO.output(20, GPIO.HIGH)
          ledOn = not ledOn

def record():
    camera = PiCamera()
    camera.iso = 800
    # camera.zoom = (0.25, 0.25, 0.5, 0.5)
    camera.start_preview()
    master = myThread(1, "master-thread", 1)
    led = myThread(2, "led-thread", 2)

    while True:
        # time.sleep(2)
        camera.capture(imgStr)
        img = Image.open(imgStr)
        sizeX = img.size[0]
        sizeY = img.size[1]
        img = img.crop((sizeX / 4, sizeY / 4, sizeX * 3 / 4, sizeY * 3 / 4))
        img = img.rotate(180)
        img.save(imageStr)

        master.start()
        led.start()

        input_state = GPIO.input(26)
        if input_state == False:
            break
    camera.stop_preview()


GPIO.setmode(GPIO.BCM)
GPIO.setwarnings(False)
GPIO.setup(26, GPIO.IN, pull_up_down=GPIO.PUD_UP)
GPIO.setup(21, GPIO.OUT)
GPIO.setup(20, GPIO.OUT)
GPIO.output(21, GPIO.LOW)
while True:
    input_state = GPIO.input(26)
    if input_state == False:
        GPIO.output(21, GPIO.HIGH)
        print("Button Pressed")
        record()
        break

GPIO.cleanup()
