from matplotlib import pyplot
import time

# Updates the data to Plot
def update(length):
    count = 0
    x = []
    y = []
    while(count < length):
        x.append(count)
        y.append(2*count)
        count = count+1
    time.sleep(2)
    return x, y

def real_time_plot():
    count = 1
    while(count <= 9):
        x, y = update(count)
        pyplot.scatter(x, y, s=30, c="r")
        # Pauses for .05 seconds
        pyplot.pause(0.05)
        count = count+1

real_time_plot()
