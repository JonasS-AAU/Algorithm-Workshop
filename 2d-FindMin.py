import numpy as np
import time
import matplotlib as mpl
import matplotlib.pyplot as plt
from numpy.random import randint

def findmin(arr):
    i = arr[0]
    for j in range(len(arr)):
        if i > arr[j]:
            i = arr[j]
    
    return i


timetaken1 = {}
timetaken2 = {}
size = 10
while size <=1000:
    A = randint(1,size,size)
    A1 = A
    A1[1] = 0
    A2 = A
    A2[size-1] = 0
    start = time.perf_counter_ns()
    findmin(A1)
    timetaken1.update({size: (time.perf_counter_ns()-start)*1000000})
    start = time.perf_counter_ns()
    findmin(A2)
    timetaken2.update({size: (time.perf_counter_ns()-start)*1000000})
    size += 10

X = [i for i in range(100, 1000, 10)]
Y = [timetaken1[i] for i in X]
Y2 = [timetaken2[i] for i in X]
fig, ax = plt.subplots(2,2,sharey='row')
ax[0,0].plot(X, Y,'ro')
ax[0,0].set_title("Best case")
ax[0,1].plot(X,Y2,'ro')
ax[0,1].set_title("Worst case")
ax[0,0].set_xlabel("Array size n")
ax[0,0].set_ylabel('Time [ms]')
ax[0,1].set_xlabel("Array size n")
ax[0,1].set_ylabel('Time [ms]')
ax[1,0].plot(X, Y,'ro')
ax[1,0].set_title("Best case")
ax[1,1].set_xscale('log')
ax[1,1].set_yscale('log')
ax[1,0].set_xscale('log')
ax[1,0].set_yscale('log')
ax[1,1].plot(X,Y2,'ro')
ax[1,1].set_title("Worst case")
ax[1,0].set_xlabel("Array size n")
ax[1,0].set_ylabel('Time [ms]')
ax[1,1].set_xlabel("Array size n")
ax[1,1].set_ylabel('Time [ms]')

fig.savefig("figure.pdf")
fig.show()
input()