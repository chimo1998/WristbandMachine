import time
import RPi.GPIO as gpio
import sys

gpio.setmode(gpio.BCM)

freq = 250

btn = 4
led = 17
motor = 25

gpio.setup(motor, gpio.OUT)
pi_pwm = gpio.PWM(pinn, freq)
pi_pwm.start(0)

gpio.setup(led, gpio.OUT)
gpio.setup(btn, gpio.IN)

while(1):
    gpio.output(led, gpio.HIGH)
    while (gpio.input(btn) == 0):
        time.sleep(0.1)
    gpio.output(led, gpio.LOW)
    pi_pwm.ChangeDutyCycle(50)
    time.sleep(1)
    pi_pwm.ChangeDutyCycle(0)
    time.sleep(0.5)
