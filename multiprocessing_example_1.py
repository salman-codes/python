from _thread import start_new_thread as snt
from time import sleep as s

tid = 1
wt = 2

def f1(n):
    global tid
    a = 0
    if n < 1:
        print("{}: {}".format("\r\nThread", tid ))
        tid += 1
        a = 1
    else:
        num = n * f1( n - 1 )  # recursive call
        print("{} != {}".format(str(n), str(num)))
        a = num
    return a

snt(f1, (3, ))
snt(f1, (2, ))
s(wt)