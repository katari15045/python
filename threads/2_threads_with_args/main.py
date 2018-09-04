from threading import Thread

def run(a, b):
    print("Thread 1 : " + str(a) + ", " + str(b))

thread_1 = Thread(target=run, args=(3, 4))
thread_1.start()
print("Main Thread")
thread_1.join()
