import threading
import time

class myWorker():

  def __init__(self):
    self.a = 1
    self.b = 2
    self.lock = threading.Lock()
  
  def modifyA(self)
    print("Modifying A : RLock Acquired: {}".format(self.lock._is_owned()))
    print("{}".format(self.lock))
    self.a = self.a + 1
    time.sleep(5)

  def modifyB(self):
    print("Modifying B : Lock Acquired: {}".format(self.lock._is_owned()))
    print("{}".format(self.lock))
    self.b = self.b - 1
    time.sleep(5)

  def modifyBoth(self):
    with self.lock:
      print("lock acquired, modifying A and B")
      print("{}".format(self.lock))
      self.modifyA()
      print("{}".format(self.lock))
      self.modifyB()
    print("{}".format(self.lock))


workerA = myWorker()
workerA.modifyBoth()

#########################################################################################
import threading
import time

class myWorker():

  def __init__(self):
    self.a = 1
    self.b = 2
    self.rlock = threading.RLock()
  
  def modifyA(self):
    with self.rlock:
      print("Modifying A : RLock Acquired: {}".format(self.rlock._is_owned()))
      print("{}".format(self.rlock))
      self.a = self.a + 1
      time.sleep(5)

  def modifyB(self):
    with self.rlock:
      print("Modifying B : RLock Acquired: {}".format(self.rlock._is_owned()))
      print("{}".format(self.rlock))
      self.b = self.b - 1
      time.sleep(5)

  def modifyBoth(self):
    with self.rlock:
      print("Rlock acquired, modifying A and B")
      print("{}".format(self.rlock))
      self.modifyA()
      print("{}".format(self.rlock))
      self.modifyB()
    print("{}".format(self.rlock))


workerA = myWorker()
workerA.modifyBoth()


# 기존의 락을 이용해서 프로그램을 실행하면 modifyA()함수를 절대 도달하지 않는다. (교착 상태)
