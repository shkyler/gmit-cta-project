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
def array_create(size):
  # seed the RNG
  np.random.seed(150)
  # return the array of the selected size
  return [np.random.randint(1000) for i in range(size)]


# Section 2 - Define the 5 Sorting Algorithms to be Used
# define the bubblesort algorithm - http://interactivepython.org/courselib/static/pythonds/SortSearch/TheInsertionSort.html
def bubble_sort(alist):
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
def insertion_sort(alist):
   for index in range(1,len(alist)):

     currentvalue = alist[index]
     position = index

     while position>0 and alist[position-1]>currentvalue:
         alist[position]=alist[position-1]
         position = position-1

     alist[position]=currentvalue

# Section 3 - Define the timer functions to be used

# define a function that takes an array and a sorting algorithm and times how long it takes to run
def timer(input_array,sort_algo):
  start = time.time()
  sort_algo(input_array)
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
def algo_trial(algo, test_size):
  # this function takes an algorithm and test size and returns the average result of 10 trials in ms - formatted to 3 decimal places
  return float("{:10.3f}".format(average_time(10,array_create(test_size),algo)*1000))

# create a column creator function
# pass a list of sorting algorithms and a test size
def col_create(algos, test_size):  
  # the algorithm will test each algorthim for a given test size ..
  col = []
  for i in algos:
    col.append(algo_trial(i, test_size))
  # .. return a list of results  
  return(col)  

# create a list of the sorting algorithms to be tested
# 'sorts' is used to index the data frame
sorts = ['Bubble Sort', 'Insertion Sort']
# 'algorithms' is a list of the function names
n = [100,250,500,750, 1000, 1250, 2500, 3750, 5000, 6250, 7500, 8750, 10000]
algorithms = [bubble_sort, insertion_sort]
# create an empty pandas data frame to store the data
data = pd.DataFrame({"size":sorts, "100":col_create(algorithms,100), "250":col_create(algorithms,250),"500":col_create(algorithms,500),"750":col_create(algorithms,750), "1000":col_create(algorithms,1000),"1250":col_create(algorithms,1250),"2500":col_create(algorithms,2500), "3750":col_create(algorithms,3750), "5000":col_create(algorithms,5000), "6250":col_create(algorithms,6250), "7500":col_create(algorithms,7500), "8750":col_create(algorithms,8750), "10000":col_create(algorithms,10000)})
data.set_index("size",inplace=True)
print(data.to_string())

for i in range(2):
  plt.plot(n,data.iloc[i])

plt.show()



# Section 5 - User Interface