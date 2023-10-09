import RPi.GPIO as gpio
import time

a = "L123456789"
b = int(a[1:8])
print(b)

# gpio.setmode(gpio.BCM)
# gpio.setup(5, gpio.OUT)

# t = 1
# 
# while True:
#     print(t)
#     gpio.output(5, t == 1)
#     t = 1 - t
#     time.sleep(5)
