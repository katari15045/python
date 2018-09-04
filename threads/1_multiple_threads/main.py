from threading import Thread

def run():
    print("Thread 1")

thread_1 = Thread(target=run)
thread_1.start()
print("Main Thread")
thread_1.join()
