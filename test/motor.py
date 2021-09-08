import sys
import time
import RPi.GPIO as gpio

gpio.setmode(gpio.BCM)

#===========================
spinTime = 1000
spinSpeed = 0.001 # lowest 0.001
spinDir = -1 #  1 -1
#===========================

motorPins = [27, 22, 23, 24]
btn = 4
led = 17

for pin in motorPins:
    gpio.setup(pin, gpio.OUT)
    gpio.output(pin, False)
gpio.setup(btn, gpio.IN)
gpio.setup(led, gpio.OUT)


seq = [[1,0,0,1],
        [1,0,0,0],
        [1,1,0,0],
        [0,1,0,0],
        [0,1,1,0],
        [0,0,1,0],
        [0,0,1,1],
        [0,0,0,1]]

step = 0
stepDir = spinDir

while True:
    gpio.output(led, True)
    while(gpio.input(btn) == 0):
        time.sleep(0.1)
    gpio.output(led, False)
    for i in range(spinTime):
        for pin in range(0,4):
            xpin = motorPins[pin]
            gpio.output(xpin, 1 == seq[step][pin])
        time.sleep(spinSpeed)

        step = (step + stepDir) % 8
    time.sleep(1)
