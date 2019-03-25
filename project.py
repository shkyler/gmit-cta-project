## Patrick Moore - GMIT - G00364753 - Comutational Thinking with Algorithms Project
# Section 1 - Import the required libraries for the project
import time
import math
import numpy as np
'''
  seed the RNG to ensure that the same lists are used all the time - it makes comparisons between
  the algorithms easier to replicate
'''
np.random.seed(0)
x = [np.random.randint(500) for i in range(10000)]

# Section 2 - Define the 5 Sorting Algorithms to be Used
# define the bubblesort algorithm
def bubble(alist):
    # outer for-loop runs from the last item in the list to the first in steps of 1
    for passnum in range(len(alist)-1,0,-1):
        # inner for-loop runs from the start of the list to the current value of passnum
        for i in range(passnum):
            # if the current item is greater than the next one
            if alist[i]>alist[i+1]:
                # then switch them
                temp = alist[i]
                alist[i] = alist[i+1]
                alist[i+1] = temp


# Section 3 - Define the timer functions to be used
def timer(a,sort_algo):
  start = time.time()
  sort_algo(a)
  end = time.time()
  return (end-start)

def average_time(runs, data, sort_algo):
  trial_times = []
  counter = 0
  while counter < runs:
    trial_times.append(timer(data,sort_algo))
    counter = counter + 1
  return (sum(trial_times)/len(trial_times))
  #return(trial_times)

print("{:10.3f}".format(average_time(10,x,bubble)*1000))

# Section 4 - Formatting the output

# Section 5 - User Interface