import usb.core
import usb.util

idVendor = 0x20d1
idProduct = 0x7007
sexual = ['女'.encode('gb18030'),'男'.encode('gb18030')]
class Printer:
    def __init__(self):
        dev = None
        while dev == None:
            try:
                dev = usb.core.find(idVendor=idVendor, idProduct=idProduct)
            except KeyboardInterrupt:
                break
            except Exception:
                continue
        dev.reset()

        if dev.is_kernel_driver_active(0):
            dev.detach_kernel_driver(0)

        dev.set_configuration()

        #cfg = dev.get_active_configuration()
        #cfg.set()

        self.dev = dev

    def __call__(self, data):
        (_id, sex, birth, name, case_num) = data
        text = '''
        SIZE 18 mm, 40 mm\r\n
        CLS\r\n
        GAP 1.9 mm, 0\r\n
        DIRECTION 1,0\r\n
        SPEED 1\r\n
        SHIFT 0\r\n
        OFFSET 0 mm\r\n
        CODEPAGE UTF-8\r\n
        TEXT 120,10,"0",90,10,10,"%s"\r\n
        TEXT 70,10,"9",90,30,30,"%s"\r\n
        TEXT 60,45,"0",90,10,10,"%s"\r\n
        TEXT 130,170,"9",90,30,30,"%s"\r\n
        BARCODE 80,160,"EAN8",55,0,90,2,2,"%s"\r\n
        PRINT 1\r\n
        ''' % (case_num, sexual[sex].decode('gb18030'), birth, name, case_num)

        self.dev.write(2, text.encode('gb18030'))
