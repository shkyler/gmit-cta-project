## Patrick Moore - GMIT - G00364753 - Comutational Thinking with Algorithms Project
# Section 1 - Import the required libraries for the project
import time
import math
import numpy as np
import pandas as pd
import matplotlib.pyplot as plt
'''
  seed the RNG to ensure that the same lists are used all the time - it makes comparisons between
  the algorithms easier to replicate
'''
# create a function to be used for generating the test arrays
def arrayCreate(size):
  # seed the RNG
  np.random.seed(100)
  # return the array of the selected size
  return [np.random.randint(1000) for i in range(size)]


# Section 2 - Define the 5 Sorting Algorithms to be Used
# define the bubblesort algorithm - http://interactivepython.org/courselib/static/pythonds/SortSearch/TheInsertionSort.html
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
                
# define the insertion sort algorithm http://interactivepython.org/runestone/static/pythonds/SortSearch/TheBubbleSort.html
# note this needs comments
def insertion(alist):
   for index in range(1,len(alist)):

     currentvalue = alist[index]
     position = index

     while position>0 and alist[position-1]>currentvalue:
         alist[position]=alist[position-1]
         position = position-1

     alist[position]=currentvalue

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
  # use a while loop to run the algorithm the specified number of times 
  counter = 0
  while counter < runs:
    trial_times.append(timer(data,sort_algo))
    counter = counter + 1
  # return the average time it takes to run the algorithm  
  return (sum(trial_times)/len(trial_times))

# Section 4 - Formatting the output

# create a function to carry out the trials
def algoTrial(algo, testSize):
  # this function takes an algorithm and test size and returns the average result of 10 trials in ms - formatted to 3 decimal places
  return float("{:10.3f}".format(average_time(10,arrayCreate(testSize),algo)*1000))

# create a column creator function
# pass a list of sorting algorithms and a test size
def colCreate(algos, testSize):  
  # the algorithm will test each algorthim for a given test size ..
  col = []
  for i in algos:
    col.append(algoTrial(i, testSize))
  # .. return a list of results  
  return(col)  

# create a list of the sorting algorithms to be tested
# 'sorts' is used to index the data frame
sorts = ['Bubble Sort', 'Insertion Sort']
# 'algorithms' is a list of the function names
algorithms = [bubble, insertion]

# create an empty pandas data frame to store the data
data = pd.DataFrame({"size":sorts, "100":colCreate(algorithms,100), "250":colCreate(algorithms,250),"500":colCreate(algorithms,500),"750":colCreate(algorithms,750), "1000":colCreate(algorithms,1000)})
print(data.to_string(index=False))

#print(data[0,1:5])
#plt.plot(n,data.loc[:,['Bubble Sort']])
#print("{:10.3f}".format(average_time(10,arr1250,bubble)*1000))


# Section 5 - User Interface