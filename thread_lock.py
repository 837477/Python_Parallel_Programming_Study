import threading
import time
import random

counter = 1
lock = threading.Lock()

# def workerA():
#     global counter
#     # lock.acquire()
#     try:
#         while counter < 1000:
#             counter += 1
#             print("Worker A is incrementing counter to {}".format(counter))
#             sleepTime = random.randint(0,1)
#             time.sleep(sleepTime)
#     finally:
#         # lock.release()
#         pass

# def workerB():
#     global counter
#     # lock.acquire()
#     try:
#         while counter > -1000:
#             counter -= 1
#             print("Worker B is decrementing counter to {}".format(counter))
#             sleepTime = random.randint(0,1)
#             time.sleep(sleepTime)
#     finally:
#         # lock.release()
#         pass

'''
Worker A is incrementing counter to 2
Worker B is decrementing counter to 1
Worker A is incrementing counter to 2
Worker B is decrementing counter to 1
Worker B is decrementing counter to 0
Worker B is decrementing counter to -1
Worker B is decrementing counter to -2
Worker B is decrementing counter to -3
Worker A is incrementing counter to -2
Worker A is incrementing counter to -1
Worker A is incrementing counter to -1
Worker B is decrementing counter to -2
Worker A is incrementing counter to 0
Worker A is incrementing counter to 1
Worker B is decrementing counter to 0
Worker A is incrementing counter to 1
Worker B is decrementing counter to 0
Worker A is incrementing counter to 1
Worker A is incrementing counter to 2
Worker B is decrementing counter to 1
Worker B is decrementing counter to 0
Worker A is incrementing counter to 1
Worker B is decrementing counter to 0
Worker A is incrementing counter to 1
Worker B is decrementing counter to 0
Worker A is incrementing counter to 1
Worker B is decrementing counter to 0
Worker B is decrementing counter to -1
Worker A is incrementing counter to 0
Worker B is decrementing counter to -1
Worker A is incrementing counter to 0
Worker B is decrementing counter to -1
Worker A is incrementing counter to 0
Worker B is decrementing counter to -1
Worker A is incrementing counter to 0
Worker B is decrementing counter to -1
Worker A is incrementing counter to 0
Worker B is decrementing counter to -1
Worker A is incrementing counter to 0
Worker A is incrementing counter to 1
Worker B is decrementing counter to 0
Worker A is incrementing counter to 1
Worker A is incrementing counter to 2
Worker A is incrementing counter to 3
Worker A is incrementing counter to 4
Worker A is incrementing counter to 5
'''

##################################################################################

def workerA():
    global counter
    lock.acquire()
    try:
        while counter < 1000:
            counter += 1
            print("Worker A is incrementing counter to {}".format(counter))
            sleepTime = random.randint(0,1)
            time.sleep(sleepTime)
    finally:
        lock.release()

def workerB():
    global counter
    lock.acquire()
    try:
        while counter > -1000:
            counter -= 1
            print("Worker B is decrementing counter to {}".format(counter))
            sleepTime = random.randint(0,1)
            time.sleep(sleepTime)
    finally:
        lock.release()

'''
Worker A is incrementing counter to 3
Worker A is incrementing counter to 4
Worker A is incrementing counter to 5
Worker A is incrementing counter to 6
Worker A is incrementing counter to 7
Worker A is incrementing counter to 8
Worker A is incrementing counter to 9
Worker A is incrementing counter to 10
Worker A is incrementing counter to 11
Worker A is incrementing counter to 12
Worker A is incrementing counter to 13
Worker A is incrementing counter to 14
Worker A is incrementing counter to 15
Worker A is incrementing counter to 16
Worker A is incrementing counter to 17
Worker A is incrementing counter to 18
Worker A is incrementing counter to 19
Worker A is incrementing counter to 20
Worker A is incrementing counter to 21
Worker A is incrementing counter to 22
Worker A is incrementing counter to 23
Worker A is incrementing counter to 24
Worker A is incrementing counter to 25
Worker A is incrementing counter to 26
Worker A is incrementing counter to 27
Worker A is incrementing counter to 28
Worker A is incrementing counter to 29
Worker A is incrementing counter to 30
Worker A is incrementing counter to 31
Worker A is incrementing counter to 32
Worker A is incrementing counter to 33
Worker A is incrementing counter to 34
Worker A is incrementing counter to 35
Worker A is incrementing counter to 36
Worker A is incrementing counter to 37
Worker A is incrementing counter to 38
Worker A is incrementing counter to 39
Worker A is incrementing counter to 40
Worker A is incrementing counter to 41
'''

def main():
    t0 = time.time()
    T1 = threading.Thread(target=workerA)
    T2 = threading.Thread(target=workerB)
    T1.start()
    T2.start()
    T1.join()
    T2.join()
    t1 = time.time()
    print("Time {}".format(t1 - t0))

if __name__ == "__main__":
    main()