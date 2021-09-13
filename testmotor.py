import time
from motor import Motor12v, Motor24v
import RPi.GPIO as gpio

led = 4

bb_motor = Motor24v(720, 10, 9, 11)
bs_motor = Motor24v(2880, 25, 8, 7)
v12 = Motor12v(17, [27,22,23,24])

v12_dir = -1
bb_dir = 1
bs_dir = 1
bs_spin = [1,0.4]

gpio.setmode(gpio.BCM)
gpio.setup(led, gpio.OUT)
gpio.output(led, gpio.HIGH)
while True:
    if (v12.check_btn() == 1):
        print("12v")
        v12.spin(v12_dir, 1)
        v12_dir = v12_dir * -1
    if (bb_motor.check_btn() == 1):
        print("bb")
        bb_motor.spin(bb_dir, 0.8)
        bb_dir = 1 - bb_dir
    if (bs_motor.check_btn() == 1):
        print("bs")
        bs_motor.spin(bs_dir, bs_spin[bs_dir])
        #bs_motor.spin(1, 0.2)
        #bs_motor.spin(0, 1)
        bs_dir = 1 - bs_dir
    time.sleep(0.1)
