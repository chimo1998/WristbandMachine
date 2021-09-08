# coding=utf-8
import usb.core
import usb.util

dev = usb.core.find(idVendor=0x20d1, idProduct=0x7007)

dev.reset()

if dev.is_kernel_driver_active(0):
    dev.detach_kernel_driver(0)
    print("yes")

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
SIZE 15 mm,40 mm\r\n
GAP 2.9 mm, 0\r\n
DIRECTION 1, 0\r\n
SHIFT 0\r\n
OFFSET 0 mm\r\n
CLS\r\n
TEXT 120,10,"0",90,12,12,"0984925-8"\r\n
TEXT 60,10,"3",90,1,1,"F"\r\n
TEXT 60,34,"0",90,12,12,"82/05/10"\r\n
TEXT 120,170,"3",90,1,1,"Nameee"\r\n
TEXT 60,170,"3",90,1,1,"Bar code"\r\n
PRINT 1\r\n
'''

# TEXT m, n
# m : 120->Top 60->Bot
# n : 10->Left 170-> Right
# 4TEXT : LT, LB, RT, RB

# OFFSET is the distance that label move futher

#TEXT 0,0,"3",90,1,1,"測試"\r\n
print(text.encode('utf-8'))
dev.write(2, text.encode('big5'))#.encode('utf-8'))
#print(text.encode('big5'))
#ep.write("SIZE 4 mm, 1.5 mm")
#ep.write("CLS")
#ep.write('TEXT 10,10,"1",0,1,1,0,"TEST"')
#ep.write("PRINT 1")

#ep.write(text)
#print(ep)
#dev.write(2,"",0)
