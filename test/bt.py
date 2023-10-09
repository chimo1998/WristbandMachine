import time
import RPi.GPIO as gpio
gpio.setmode(gpio.BCM)
gpio.setup(23, gpio.IN)
gpio.setup(24, gpio.IN)

while(1):
    print("hum1 : " + str(gpio.input(23)))
    print("hum2 : " + str(gpio.input(24)))
    time.sleep(0.2)
    print()
    print()
