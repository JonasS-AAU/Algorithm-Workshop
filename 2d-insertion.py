import numpy as np
import time
import matplotlib as mpl
import matplotlib.pyplot as plt
from numpy.random import randint


def insertionSort(a):
    for j in range(1,len(a)):
        key = a[j]
        i = j-1
        while i>=0 and key < a[i]:
            a[i+1] = a[i]
            i=i-1
        a[i+1] = key

def printArr(a):
    for j in range(len(a)):
        print(a[j], end = " ")
'''
a = [67,23,7,38,58,39]
print("Before:")
printArr(a)
insertionSort(a)
print("\nAfter:")
printArr(a)
'''

timetaken1 = {}
timetaken2 = {}
size = 10
while size <=1000:
    A = randint(1,size,size)
    A.sort()
    A1 = randint(1,size,size)
    A1.sort()
    A2 = A[::-1]
    start = time.perf_counter_ns()
    insertionSort(A2)
    timetaken1.update({size: (time.perf_counter_ns()-start)/1000000})
    start = time.perf_counter_ns()
    insertionSort(A1)
    timetaken2.update({size: (time.perf_counter_ns()-start)/1000000})
    size += 10

X = [i for i in range(100, 1000, 10)]
Y = [timetaken1[i] for i in X]
Y2 = [timetaken2[i] for i in X]
fig, ax = plt.subplots(2,2,sharey='row')
ax[0,1].plot(X, Y,'ro')
ax[0,1].set_title("Worst case")
ax[0,0].plot(X,Y2,'ro')
ax[0,0].set_title("Best case")
ax[0,0].set_xlabel("Array size n")
ax[0,0].set_ylabel('Time [ms]')
ax[0,1].set_xlabel("Array size n")
ax[0,1].set_ylabel('Time [ms]')
ax[1,1].plot(X, Y,'ro')
ax[1,0].set_title("Best case")
ax[1,1].set_xscale('log')
ax[1,1].set_yscale('log')
ax[1,0].set_xscale('log')
ax[1,0].set_yscale('log')
ax[1,0].plot(X,Y2,'ro')
ax[1,1].set_title("Worst case")
ax[1,0].set_xlabel("Array size n")
ax[1,0].set_ylabel('Time [ms]')
ax[1,1].set_xlabel("Array size n")
ax[1,1].set_ylabel('Time [ms]')

fig.savefig("figure.pdf")
fig.show()
input()