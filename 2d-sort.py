# Python program for the above approach

# Bucket sort for numbers
# having integer part
import numpy as np
import time
import matplotlib as mpl
import matplotlib.pyplot as plt
from numpy.random import randint
import math

# Python program for counting sort
# which takes negative numbers as well

# The function that sorts the given arr[]
def countSort(arr):
	max_element = int(max(arr))
	min_element = int(min(arr))
	range_of_elements = max_element - min_element + 1
	# Create a count array to store count of individual
	# elements and initialize count array as 0
	count_arr = [0 for _ in range(range_of_elements)]
	output_arr = [0 for _ in range(len(arr))]

	# Store count of each character
	for i in range(0, len(arr)):
		count_arr[arr[i]-min_element] += 1

	# Change count_arr[i] so that count_arr[i] now contains actual
	# position of this element in output array
	for i in range(1, len(count_arr)):
		count_arr[i] += count_arr[i-1]

	# Build the output character array
	for i in range(len(arr)-1, -1, -1):
		output_arr[count_arr[arr[i] - min_element] - 1] = arr[i]
		count_arr[arr[i] - min_element] -= 1

	# Copy the output array to arr, so that arr now
	# contains sorted characters
	for i in range(0, len(arr)):
		arr[i] = output_arr[i]

	return arr


# Driver program to test above function
arr = [-5, -10, 0, -3, 8, 5, -1, 10]
ans = countSort(arr)
print("Sorted character array is " + str(ans))





timetaken1 = {}
timetaken2 = {}
size = 10
while size <=10000:
    A = randint(1,size,size)
    start = time.perf_counter_ns()
    countSort(A)
    timetaken1.update({size: (time.perf_counter_ns()-start)*1000000})
    start = time.perf_counter_ns()
    countSort(A)
    timetaken2.update({size: (time.perf_counter_ns()-start)*1000000})
    size += 10

X = [i for i in range(100, 10000, 10)]
Y = [timetaken1[i] for i in X]
Y2 = [timetaken2[i] for i in X]
fig, ax = plt.subplots(1,2,sharey='row')
ax[0].plot(X, Y,'ro')
ax[0].set_title("Best case")
ax[1].plot(X,Y2,'ro')
ax[1].set_title("Worst case")
ax[0].set_xlabel("Array size n")
ax[0].set_ylabel('Time [ms]')
ax[1].set_xlabel("Array size n")
ax[1].set_ylabel('Time [ms]')

fig.savefig("figure.pdf")
fig.show()
input()
