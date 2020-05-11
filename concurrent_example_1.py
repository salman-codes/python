import threading as td
import time as t

def f1():
    print("Thread-Starting")
    t.sleep(10)
    print("Thread-Ending")
def f2():
    while True:
        print(True)
        t.sleep(4)

ndt = td.Thread(target = f1)
dt = td.Thread(target = f2)
dt.setDaemon(True)
dt.start()
ndt.start()