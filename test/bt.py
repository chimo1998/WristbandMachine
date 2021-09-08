import time
import RPi.GPIO as gpio
gpio.setmode(gpio.BCM)
gpio.setup(4, gpio.IN)

while(1):
    print(gpio.input(4))
    time.sleep(0.1)
