from reader import Reader
from printer import Printer
import time
from motor import Motor12v, Motor24v
import RPi.GPIO as gpio
import pygame
import hashlib
import json

led = 25
red_led = 10
green_led = 9

hum1 = 23
hum2 = 24

band = 16

sounddir = "sound"

CASE_URL = "https://webf.cych.org.tw/IpdInfo/api/PatSmpInfo?id1=%s&id2=%s&Key=%s"
CASE_VAR = "1"
CASE_BASE_HASH = "tPptRZeYS5472rEoZBd48QmkxU2Sofu5kcoHnFjHGyqt7ltKSyKHLlnUCex54ULF"

temp = False
def get_case_num(id_num):
    con = "%s^%s^%s" % (CASE_BASE_HASH, CASE_VAR, id_num)
    sha1 = hashlib.sha1()
    sha1.update(con.encode('utf-8'))
    hashed = sha1.hexdigest()
    try:
        r = requests.get(CASE_URL % (CASE_VAR, id_num, hashed))
        mj = r.json()
        print(mj)
        # return mj["pat_no"]
        return "01234567"
    except:
        global temp
        print(temp)
        temp = not temp
        if temp:
            return "01234567"
        return None

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

# setup sound
pygame.mixer.init(44200)
pygame.mixer.music.set_volume(1.0)

music_dir = "/home/pi/desktop/WristbandMachine/sound/"
def play_sound(f):
    pygame.mixer.music.load(music_dir+f)
    pygame.mixer.music.play()

aat = 0

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

        # get case number from server
        case_num = get_case_num(data[0])
        print(data)
        aat = 1-aat
        if aat==1 and not case_num == None:  # case not found
            play_sound("1.mp3")
            continue

        # case found
        play_sound("2.mp3")

        data = data + (case_num,)
        print(data)
        gpio.output(led, gpio.LOW)
        # bb roll front
        bb_motor.spin(1, 0.8)
        # v12 roll down
        v12.spin(-1, 1)
        # bs roll in
        bs_motor.spin(1, 0.4)
        # print
        printer(data)
        time.sleep(1.3)
        # bs roll out
        bs_motor.spin(0, 1)
        # bs roll in
        #bs_motor.spin(1, 1)
        # v12 roll up
        v12.spin(1, 1)
        # bb roll back
        bb_motor.spin(0, 0.8)
        # power up straper
        gpio.output(green_led, gpio.HIGH)
        gpio.output(red_led, gpio.LOW)
        # start checking hand
        while (gpio.input(hum1) or gpio.input(hum2)):
            pygame.mixer.music.load(music_dir+"3.mp3")
            pygame.mixer.music.play()
            while pygame.mixer.music.get_busy() and (( gpio.input(hum1) or gpio.input(hum2) )):
                pass
            time.sleep(0.1)
        pygame.mixer.music.stop()
        time.sleep(2)
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

        play_sound("4.mp3")

    except KeyboardInterrupt:
        break

    except Exception:
        time.sleep(2)
        reader.previous_card_num = ""

