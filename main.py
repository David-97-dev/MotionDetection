import RPi.GPIO as GPIO
import time

GPIO.setwarnings(False)
GPIO.setmode(GPIO.BOARD)
GPIO.setup(15, GPIO.IN)
while True:
    i = GPIO.input(15)
    if i == 0:
        print("No motion", i)
        time.sleep(6)
    elif i == 1:
        print("Motion Detected", i)
        time.sleep(6)

