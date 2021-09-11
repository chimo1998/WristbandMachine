#coding=utf-8
import usb.core
import usb.util

dev = usb.core.find(idVendor=0x20d1, idProduct=0x7007)

dev.reset()

if dev.is_kernel_driver_active(0):
    dev.detach_kernel_driver(0)

dev.set_configuration()

cfg = dev.get_active_configuration()
cfg.set()
intf = cfg[(0,0)]

ep = usb.util.find_descriptor(
    intf,
    custom_match = \
    lambda e: \
        usb.util.endpoint_direction(e.bEndpointAddress) == \
        usb.util.ENDPOINT_OUT)
text = '''
SIZE 18 mm,40 mm\r\n
CLS\r\n
GAP 1.9 mm, 0\r\n
DIRECTION 1, 0\r\n
SPEED 1\r\n
SHIFT 0\r\n
OFFSET 0 mm\r\n
CODEPAGE UTF-8\r\n
TEXT 120,10,"0",90,10,10,"0984925-8"\r\n
TEXT 70,10,"9",90,30,30,"女"\r\n
TEXT 60,45,"0",90,10,10,"82/05/10"\r\n
TEXT 130,170,"9",90,30,30,"王小明"\r\n
BARCODE 80,160,"EAN8",55,0,90,2,2,"09849258"\r\n
PRINT 1\r\n
'''

# TEXT m, n
# m : 120->Top 60->Bot
# n : 10->Left 170-> Right
# 4TEXT : LT, LB, RT, RB

# OFFSET is the distance that label move futher

# utf8 gb2312 gb18030 big5
dev.write(2, text.encode('gb18030'))#.encode('utf-8'))
