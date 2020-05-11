
import threading
def countdown():
    x = 100000000
    while x > 0:
        x -= 1

def countup():
    y = 0
    while y < 100000000:
        y += 1

thread_1 = threading.Thread(target=countdown)
thread_2 = threading.Thread(target=countup)
thread_1.start()
thread_2.start()
thread_1.join()
thread_2.join()