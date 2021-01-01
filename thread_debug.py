import threading
import time

def myThread():
    print("Thread {} start".format(threading.currentThread().getName()))
    time.sleep(5)
    print("Thread {} end".format(threading.currentThread().getName()))

if __name__ == "__main__":
    for i in range(4):
        threadName = "Thread-" + str(i)
        T = threading.Thread(name=threadName, target=myThread)
        T.start()

# 각각의 스레드에 명명을 해주면 추후 디버깅 하기 편리해짐