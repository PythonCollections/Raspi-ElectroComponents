import RPi.GPIO as GPIO
import time

GPIO.setmode(GPIO.BOARD)

Trigger = 23
Echo = 24

GPIO.setup(Trigger,GPIO.OUT)
GPIO.output(Trigger,0)

GPIO.setup(Echo,GPIO.IN)
time.sleep(0.1)

print("Measurement Starting")

GPIO.output(Trigger,1)
time.sleep(0.00001)
GPIO.output(Trigger,0)

while GPIO.input(Echo) == 0:
    pass
start = time.time()

while GPIO.input(Echo) == 1:
    pass
stop = time.time()

print ((stop - start * 170))


