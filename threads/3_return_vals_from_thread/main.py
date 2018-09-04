from threading import Thread

def run(ret, a, b):
    print("Thread 1 : " + str(a) + ", " + str(b))
    ret.append(a+b)

ret = []
thread_1 = Thread(target=run, args=(ret, 3, 4, ))
thread_1.start()
print("Main Thread")
thread_1.join()
print(ret)
