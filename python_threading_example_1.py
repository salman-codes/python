import time as t
import _thread as td

def f1(x, y):
    i = 0
    while i <= 4.0:
        print("Running Thread %s\n" % x)
        t.sleep(y)
        i = i + 1

    print("Thread %s Completed" % x)

td.start_new_thread(f1, ("Thread A Started", 3))
td.start_new_thread(f1, ("Thread B Started", 4))
td.start_new_thread(f1, ("Thread C Started", 1))