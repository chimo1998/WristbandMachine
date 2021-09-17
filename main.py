from reader import Reader
from printer import Printer
import time
from motor import Motor12v, Motor24v
import RPi.GPIO as gpio


led = 25
red_led = 10
green_led = 9

hum1 = 23
hum2 = 24

band = 15

bb_motor = Motor24v(720, 19, 26)
bs_motor = Motor24v(2880, 5, 6)
v12 = Motor12v([4,17,27,22])

reader = Reader()
printer = Printer()

gpio.setmode(gpio.BCM)
gpio.setup(led, gpio.OUT)
gpio.setup(red_led, gpio.OUT)
gpio.setup(green_led, gpio.OUT)
gpio.setup(hum1, gpio.IN)
gpio.setup(hum2, gpio.IN)
gpio.setup(band, gpio.OUT)
gpio.output(band, gpio.HIGH)
gpio.setwarnings(False)

gpio.output(red_led, gpio.HIGH)
gpio.output(green_led, gpio.LOW)
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
        gpio.output(green_led, gpio.HIGH)
        gpio.output(red_led, gpio.LOW)
        while (gpio.input(hum1) or gpio.input(hum2)):
            time.sleep(0.1)
        gpio.output(band, gpio.LOW)
        time.sleep(1)
        gpio.output(band, gpio.HIGH)
        time.sleep(1)
        while not ((gpio.input(hum1) and gpio.input(hum2))):
            time.sleep(0.1)
        gpio.output(green_led, gpio.LOW)
        gpio.output(red_led, gpio.HIGH)
        gpio.output(band, gpio.LOW)
        time.sleep(1)
        gpio.output(band, gpio.HIGH)
        time.sleep(1)

    except Exception:
        time.sleep(2)
        reader.previous_card_num = ""

