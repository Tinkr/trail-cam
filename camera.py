from picamera import PiCamera
from time import sleep
import RPi.GPIO as GPIO

GPIO.setmode(GPIO.BOARD)
GPIO.setup(22, GPIO.OUT)
GPIO.output(22,True)


camera = PiCamera()

camera.start_preview()
sleep(10)
camera.annotate_text = "Hello world"
camera.capture('/home/pi/Desktop/image1.jpg')
camera.stop_preview()

GPIO.output(22,False) 

