#codeing=utf-8
from smartcard.System import readers

SelectAPDU = [ 0x00, 0xA4, 0x04, 0x00, 0x10, 0xD1, 0x58, 0x00, 0x00, 0x01, 0x00, 0x00, 0x00, 0x00, 0x00, 0x00, 0x00, 0x00, 0x00, 0x11, 0x00 ]
ReadProfileAPDU = [ 0x00, 0xca, 0x11, 0x00, 0x02, 0x00, 0x00 ]
class Reader:
    def __init__(self):
        self.previous_card_num = ""
        r = None
        while r == None or len(r) == 0:
            try:
                r = readers()
            except Exception:
                continue
        reader = r[0]
        self.reader = reader

    def read(self):
        conn = None
        try:
            conn = self.reader.createConnection()
            conn.connect()
        except Exception:
            self.previous_card_num = ""
            return None
        try:
            data, sw1, sw2 = conn.transmit(SelectAPDU)
            data, sw1, sw2 = conn.transmit(ReadProfileAPDU)
        except Exception:
            print("Transmit error")
            return None

        card_num = ''.join(chr(i) for i in data[0:12])
        if card_num == self.previous_card_num:
            return "same"
            #return None

        self.previous_card_num = card_num

        namecount = sum([0 if a==0 else 1 for a in data[12:32]])
        name = '{}'.format(bytes(data[12:(12+namecount+namecount%2)]).decode('big5'))
        id_num = ''.join(chr(i) for i in data[32:42])
        case_num = self.id_to_case(id_num)
        birth = '%s/%s/%s' % (''.join(chr(i) for i in data[43:45]), ''.join(chr(i) for i in data[45:47]), ''.join(chr(i) for i in data[47:49]))
        sex = 1 if ''.join(chr(i) for i in data[49:50]) == "M" else 0
        return (case_num, sex, birth, name)

    def id_to_case(self, _id):
        # Search
        return "00000" + _id[4:7]
