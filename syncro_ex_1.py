#syncronization

from threading import *

class multbl:
    def __init__(self):
        self.l = Lock()

    def tbl(self,n):
        self.l.acquire()
        for i in range(1,11):
            print(i*n)
        print()
        self.l.release()
        
obj1 = multbl()
obj1 = multbl()
obj1 = multbl()

th1 = Thread(target = obj1.tbl,args = (21,))
th2 = Thread(target = obj1.tbl,args = (2,))
th3 = Thread(target = obj1.tbl,args = (15,))

th1.start()
th2.start()
th3.start()
