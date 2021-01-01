import threading
import time

def standardThread():
    print("Start standard")
    time.sleep(10)
    print("End standard")

def daemonThread():
    while True:
        print("Sending signal")
        time.sleep(2)

if __name__ == "__main__":
    ST = threading.Thread(target=standardThread)
    DT = threading.Thread(target=daemonThread)
    DT.setDaemon(True)
    
    DT.start()
    ST.start()