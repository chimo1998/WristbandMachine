import sys
import time
import RPi.GPIO as gpio

led = 4
#==== gray motor ====
spinTime = 4096
spinSpeed = 0.001
seq = [[1,0,0,1],
        [1,0,0,0],
        [1,1,0,0],
        [0,1,0,0],
        [0,1,1,0],
        [0,0,1,0],
        [0,0,1,1],
        [0,0,0,1]]
#====================

class Motor12v:
    def __init__(self, pins):
        gpio.setmode(gpio.BCM)
        for pin in pins:
            gpio.setup(pin, gpio.OUT)
        self.pins = pins
        self.step = 0

    def spin(self, direction, turns):
        step = self.step
        for i in range(int(turns * spinTime)):
            for pin in range(0,4):
                xpin = self.pins[pin]
                gpio.output(xpin, 1 == seq[step][pin])
            time.sleep(spinSpeed)
            step = (step + direction) % 8
        self.step = step


class Motor24v:
    def __init__(self, freq, pin, direction):
        gpio.setmode(gpio.BCM)
        gpio.setup(pin, gpio.OUT)
        motor = gpio.PWM(pin, freq)
        motor.start(0)
        self.motor = motor

        gpio.setup(direction, gpio.OUT)
        self.direction = direction

    def spin(self, direction, sec):
        gpio.output(self.direction, direction)
        self.motor.ChangeDutyCycle(50)
        time.sleep(sec)
        self.motor.ChangeDutyCycle(0)
