import usb.core
import usb.util

dev = usb.core.find(idVendor=0x20d1, idProduct=0x7007)

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
SIZE 40 mm,15 mm\r\n
GAP 2.9 mm, 0\r\n
DIRECTION 0\r\n
SHIFT 0\r\n
OFFSET 0\r\n
CLS\r\n
TEXT 0,25,"1",0,1,1,"AAAAAAAAAAAAAAAA"\r\n
TEXT 100,20,"3",0,1,1,"測試"\r\n
TEXT 100,40,"3",0,1,1,"TEST"\r\n
PRINT 1\r\n
'''

#print(text.encode('utf-8'))
dev.write(2, text.endcode('big5'))#.encode('utf-8'))
#print(text.encode('big5'))
#ep.write("SIZE 4 mm, 1.5 mm")
#ep.write("CLS")
#ep.write('TEXT 10,10,"1",0,1,1,0,"TEST"')
#ep.write("PRINT 1")

#ep.write(text)
#print(ep)
#dev.write(2,"",0)
