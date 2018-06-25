import RPi._GPIO as GPIO
import time


GPIO.setmode(GPIO.BCM)

ControlPin = [17,18,27,22]

for pin in ControlPin:
    GPIO.setup(pin,GPIO.OUT)
    GPIO.setup(pin,GPIO.LOW)

seq = [[1,0,0,0],
       [1,1,0,0],
       [0,1,0,0],
       [0,1,1,0],
       [0,0,1,0],
       [0,0,1,1],
       [0,0,0,1],
       [1,0,0,1]]

for i in range(512):
    for halfstep in range(8):
        for pin in range(4):
            a = ControlPin[pin],seq[halfstep][pin]
            GPIO.output(ControlPin[pin],seq[halfstep][pin])
            time.sleep(0.001)


GPIO.cleanup()
