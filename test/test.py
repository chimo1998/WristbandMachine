# coding=utf-8
import time
import RPi.GPIO as gpio
import sys

gpio.setmode(gpio.BCM)

while(1):
    gpio.setup(17, gpio.OUT)
    gpio.output(17, t==0)
    t = 1 - t
    time.sleep(0.2)
    print("æ¸")
