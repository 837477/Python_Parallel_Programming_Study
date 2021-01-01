import os

def child():
    print("Child process with PID = %d" %(os.getpid()))

def parent():
    print("Parent process with PID = %d" %(os.getpid()))
    newRef = os.getpid()
    if newRef == 0:
        child()
    else:
        print("Parent process and our child process has PID = %d" %(newRef))

if __name__ == "__main__":
    parent()