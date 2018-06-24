import RPi._GPIO as GPIO
import time

GPIO.setmode(GPIO.BCM)

Output Pis = [17,22,25,26]

for items in Outputs:
    GPIO.setup(items,GPIO.OUT)
