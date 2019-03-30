## Patrick Moore - GMIT - G00364753 - Comutational Thinking with Algorithms Project
# Section 1 - Import the required libraries for the project
import time
import math
import numpy as np
import pandas as pd
'''
  seed the RNG to ensure that the same lists are used all the time - it makes comparisons between
  the algorithms easier to replicate
'''
# create the arrays to be sorted 
# seed the RNG so the program runs the same everytime
np.random.seed(100)
arr100 = [np.random.randint(1000) for i in range(100)]
arr250 = [np.random.randint(1000) for i in range(250)]
arr500 = [np.random.randint(1000) for i in range(500)]
arr750 = [np.random.randint(1000) for i in range(750)]
arr1000 = [np.random.randint(1000) for i in range(1000)]
arr1250 = [np.random.randint(1000) for i in range(1250)]
arr2500 = [np.random.randint(1000) for i in range(2500)]
arr3750 = [np.random.randint(1000) for i in range(3750)]
arr5000 = [np.random.randint(1000) for i in range(5000)]
arr6250 = [np.random.randint(1000) for i in range(6250)]
arr7500 = [np.random.randint(1000) for i in range(7500)]
arr8750 = [np.random.randint(1000) for i in range(8750)]
arr10000 = [np.random.randint(1000) for i in range(10000)]


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

# define a function that takes an array and a sorting algorithm and times how long it takes to run
def timer(a,sort_algo):
  start = time.time()
  sort_algo(a)
  end = time.time()
  return (end-start)

# define a function to calucate the average running time of a sorting algorithm
def average_time(runs, data, sort_algo):
  # use an array to store the results of each trial
  trial_times = []
  # use a while loop to run time the algorithm th e specified number of times 
  counter = 0
  while counter < runs:
    trial_times.append(timer(data,sort_algo))
    counter = counter + 1
  # return the average time it take sto run the algorithm  
  return (sum(trial_times)/len(trial_times))

# Section 4 - Formatting the output
# create a list of the sorting algorithms to be tested
sorts = ['Bubble Sort']
# run the trials and store results in lists
trial100 = [float("{:10.3f}".format(average_time(10,arr100,bubble)*1000))]
trial250 = [float("{:10.3f}".format(average_time(10,arr250,bubble)*1000))]
trial500 = [float("{:10.3f}".format(average_time(10,arr500,bubble)*1000))]
trial750 = [float("{:10.3f}".format(average_time(10,arr750,bubble)*1000))]
trial1000 = [float("{:10.3f}".format(average_time(10,arr1000,bubble)*1000))]
trial1250 = [float("{:10.3f}".format(average_time(10,arr1250,bubble)*1000))]
trial2500 = [float("{:10.3f}".format(average_time(10,arr2500,bubble)*1000))]
trial3750 = [float("{:10.3f}".format(average_time(10,arr3750,bubble)*1000))]
trial5000 = [float("{:10.3f}".format(average_time(10,arr5000,bubble)*1000))]
trial6250 = [float("{:10.3f}".format(average_time(10,arr6250,bubble)*1000))]
trial7500 = [float("{:10.3f}".format(average_time(10,arr7500,bubble)*1000))]
trial8750 = [float("{:10.3f}".format(average_time(10,arr8750,bubble)*1000))]
trial10000 = [float("{:10.3f}".format(average_time(10,arr10000,bubble)*1000))]

# create an empty pandas data frame to store the data
data = pd.DataFrame({"size":sorts, "100":trial100,"250":trial250,"500":trial500,"750":trial750,"1000":trial1000,"1250":trial1250,"2500":trial1250,"3750":trial3750,"5000":trial5000,"6250":trial6250,"7500":trial7500, "8750":trial8750, "10000":trial10000})
print(data.to_string(index=False))
#print("{:10.3f}".format(average_time(10,arr1250,bubble)*1000))


# Section 5 - User Interface