import numpy as np
import time
import matplotlib as mpl
import matplotlib.pyplot as plt
from numpy.random import randint

def Itbinarysearch(arr,x):
    low=0
    high = len(arr)-1

    while high - low >= 1:
        mid = (low + high)//2

        if arr[mid] == x:
            return mid

        elif arr[mid] < x:
            low = mid+1

        elif arr[mid] > x:
            high = mid-1

    if arr[high] == x:
        return high
    else:
        return -1

def Rebinarysearch(arr,low,high,x):
    if high>= 1:
        mid = (low+high)//2
        print(low)
        print(mid)
        print(high)
        print("\n")

        if arr[mid] == x:
            return mid
        elif arr[mid] < x:
            return Rebinarysearch(arr,mid+1,high,x)
        elif arr[mid] > x:
            return Rebinarysearch(arr,low,mid-1,x)

    else: 
        return -1
'''
A = randint(1,10000,10000)
v = 999999
start = time.time()
print(time.time())
result = Itbinarysearch(A,v)
print(time.time())
end = time.time()
timetaken = (end-start)*1000

if result == -1:
    print("is not here")
else:
    print("is here")

#print(start)
#print(end)
print(timetaken)

'''
timetaken1 = {}
timetaken2 = {}
size = 10
while size <=10000:
    A = randint(1,size,size)
    A.sort()
    v1 = A[(0+(len(A)-1))//2]
    v2 = 999999
    start = time.perf_counter_ns()
    Itbinarysearch(A,v1)
    timetaken1.update({size: (time.perf_counter_ns()-start)/1000000})
    start = time.perf_counter_ns()
    Itbinarysearch(A,v2)
    timetaken2.update({size: (time.perf_counter_ns()-start)/1000000})
    size += 10

timetaken = {}
size = 10
while size <=1000:
    A = randint(1,size,size)
    A.sort()
    tmp = 0
    for i in range(len(A)):
        v1 = A[i]
        start = time.perf_counter_ns()
        Itbinarysearch(A,v1)
        tmp += ((time.perf_counter_ns()-start)/1000000)
    timetaken.update({size: (tmp/size)})
    size += 10
'''


X = [i for i in range(100, 1000, 10)]
Y = [timetaken[i] for i in X]
fig, ax = plt.subplots(1,2)
ax[0].plot(X,Y,'ro')
ax[1].plot(X,Y,'ro')
ax[0].set_title("average case")
ax[0].set_xlabel("Array size n")
ax[0].set_ylabel("Time [ms]")
ax[1].set_title("average case")
ax[1].set_xlabel("Array size n")
ax[1].set_ylabel("Time [ms]")
ax[1].set_xscale('log')
ax[1].set_yscale('log')

'''
X = [i for i in range(100, 10000, 10)]
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


fig.show()
input()