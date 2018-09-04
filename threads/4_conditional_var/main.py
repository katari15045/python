from threading import Thread
from threading import Condition

def run(condition):
    condition.acquire()
    condition.wait()
    condition.release()
    print("Thread 1")

condition = Condition()
thread_1 = Thread(target=run, args=(condition, ))
thread_1.start()
print("Main Thread")
condition.acquire()
condition.notifyAll()
condition.release()
thread_1.join()
