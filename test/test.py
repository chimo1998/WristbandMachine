import RPi.GPIO as gpio
import time

gpio.setmode(gpio.BCM)
gpio.setup(5, gpio.OUT)

t = 1

while True:
    print(t)
    gpio.output(5, t == 1)
    t = 1 - t
    time.sleep(5)
