from reader import Reader
from printer import Printer

reader = Reader()
printer = Printer()

while(True):
    t = None
    while(t == None):
        #try:
        t = reader.read()
        #except Exception:
        #    pass
    print(t)
    #printer(t[0],t[1],t[2],t[3])
