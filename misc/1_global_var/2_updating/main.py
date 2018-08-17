global count

def foo():
    global count
    count = count+1

count = 0
foo()
print(count)
