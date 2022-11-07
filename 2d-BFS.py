import numpy as np
import time
import matplotlib as mpl
import matplotlib.pyplot as plt
from numpy import random
from numpy.random import randint


def graphgen(st):
    D = {}
    for i in range(st):
        tempL = []
        verticeRange = random.randint(0,st-1)
        for j in range(verticeRange):
            rN = random.randint(0,st-1)
            tempL.append(rN)

        D[i] = tempL
    return D


queue = []
visited = []
def BFS(Graph, root):
    visited.append(root)
    queue.append(root)

    while queue:
        v = queue.pop(0)

        for n in Graph[v]:
            if n not in visited:
                visited.append(n)
                queue.append(n)

timetaken1 = {}
timetaken2 = {}
size = 10
while size <=1000:
    A = graphgen(size)
    start = time.perf_counter_ns()
    BFS(A, size/2)
    timetaken1.update({size: (time.perf_counter_ns()-start)/1000000})
    start = time.perf_counter_ns()
    BFS(A, 0)
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