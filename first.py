import threading
import time

def threadworker(i):
    print(str(i) + " Thread has entered the 'Running' State")
    time.sleep(i)
    print(str(i) + " Thread is terminating")

if __name__ == "__main__":
    for i in range(1, 4):
        T = threading.Thread(target=threadworker, args=(i,))
        T.start()
    