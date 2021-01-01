import threading
from multiprocessing import Process
import time
import os

def MyTask():
    print("Starting")
    time.sleep(2)

if __name__ == "__main__":
    time_0 = time.time()
    threads = []

    for i in range(10):
        T = threading.Thread(target=MyTask)
        T.start()
        threads.append(T)

    time_1 = time.time()
    print("Total time for creating 10 threads: {} seconds".format(time_1 - time_0))

    for thread in threads:
        thread.join()
    
    time_2 = time.time()

    processes = []
    for i in range(10):
        P = Process(target=MyTask)
        P.start()
        processes.append(P)
    
    time_3 = time.time()
    print("Total time for creating 10 processes: {} seconds".format(time_3 - time_2))
    for process in processes:
        process.join()

'''
프로세스에서의 시간이 스레드보다 10정도 더 걸렸다.
이를 해결하려면 모든 프로세스 및 스레드를 시작할 때 풀에 저장해 생성에 많은 부하가 발생하지 않도록 해야한다.
'''