from reader import Reader
from printer import Printer
import time
from motor import Motor12v, Motor24v
import RPi.GPIO as gpio


led = 25
pir = 14

bb_motor = Motor24v(720, 19, 16, 26)
bs_motor = Motor24v(2880, 5, 20, 6)
v12 = Motor12v(21, [4,17,27,22])

reader = Reader()
printer = Printer()

gpio.setmode(gpio.BCM)
gpio.setup(led, gpio.OUT)
gpio.setup(pir, gpio.OUT)
gpio.output(pir, gpio.HIGH)

while(True):
    try:
        print("in main")
        gpio.output(led, gpio.HIGH)
        data = None
        while(data == None):
            data = reader.read()
            if data == "same":
                data = None
                continue
            gpio.output(pir, gpio.HIGH)

        print(data)
        gpio.output(led, gpio.LOW)
        # bb roll front
        bb_motor.spin(1, 0.8)
        # v12 roll down
        v12.spin(-1, 1)
        # bs roll in
        #bs_motor.spin(1, 0.4)
        # print
        printer(data)
        time.sleep(1.3)
        # bs roll out
        bs_motor.spin(0, 1)
        # bs roll in
        bs_motor.spin(1, 1)
        # v12 roll up
        v12.spin(1, 1)
        # bb roll back
        bb_motor.spin(0, 0.8)
        # power up straper
        gpio.output(pir, gpio.LOW)

        time.sleep(0.1)
    except Exception:
        time.sleep(2)
        reader.previous_card_num = ""

