## Patrick Moore - GMIT - G00364753 - Comutational Thinking with Algorithms Project
# As this program takes a while to load - print a warning to the user
print("Please be patient while program loads......")

# Section 1 - Import the required libraries for the project
import time
import math
import numpy as np
import pandas as pd
import matplotlib.pyplot as plt

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
# define the selection sorting algorithm - http://interactivepython.org/runestone/static/pythonds/SortSearch/TheSelectionSort.html
# note - this needs comments
def selection_sort(alist):
   for fillslot in range(len(alist)-1,0,-1):
       positionOfMax=0
       for location in range(1,fillslot+1):
           if alist[location]>alist[positionOfMax]:
               positionOfMax = location

       temp = alist[fillslot]
       alist[fillslot] = alist[positionOfMax]
       alist[positionOfMax] = temp

# define the merge sort algorithm - http://interactivepython.org/runestone/static/pythonds/SortSearch/TheMergeSort.html
# note - this needs comments
def merge_sort(alist):
    #print("Splitting ",alist)
    if len(alist)>1:
        mid = len(alist)//2
        lefthalf = alist[:mid]
        righthalf = alist[mid:]

        merge_sort(lefthalf)
        merge_sort(righthalf)

        i=0
        j=0
        k=0
        while i < len(lefthalf) and j < len(righthalf):
            if lefthalf[i] < righthalf[j]:
                alist[k]=lefthalf[i]
                i=i+1
            else:
                alist[k]=righthalf[j]
                j=j+1
            k=k+1

        while i < len(lefthalf):
            alist[k]=lefthalf[i]
            i=i+1
            k=k+1

        while j < len(righthalf):
            alist[k]=righthalf[j]
            j=j+1
            k=k+1
    #print("Merging ",alist)

# define the counting sort algorithm - 
# note - this needs comments

# Section 3 - Define the timer functions to be used

# create a function to be used for generating the test arrays
def array_create(size):
  # seed the RNG
  np.random.seed(150)
  # return the array of the selected size
  return [np.random.randint(1000) for i in range(size)]

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

# define a function that creates a pandas dataframe based on a data dictionary passed to it
def df_create(data_dict):
  # create the data frame, set the index to the "size" field and return the dataframe
  data = pd.DataFrame(data_dict)
  data.set_index("size",inplace=True)
  return data

# define a function that creates a pandas dataframe and plot the results based on the data dictionary, test input sizes and sorting algorithms passed to it
def results_plot(data_dict, test_size, sort_algos):
  # create a pandas dataframe based on the data passed to it
  data = df_create(data_dict)
  # loop through the list of test sizes
  for i in range(len(sorts)):
    plt.plot(test_size, data.iloc[i], label=sort_algos[i])
  plt.xlabel("Input Size, n")  
  plt.ylabel("Average Running Time, milliseconds")
  plt.title ("Benchmarking Sorting Algorithms")
  plt.legend()
  plt.show()

# define a function that exports the results of the trial to a csv file
def results_export(data_dict):
  data = df_create(data_dict)
  data.to_csv('benchmark.csv')

# Section 5 - User Interface

# create a list of the sorting algorithms to be tested
# 'sorts' is used to index the data frame
sorts = ['Bubble Sort', 'Insertion Sort', 'Selection Sort', 'Merge Sort']
# 'algorithms' is a list of the function names
algorithms = [bubble_sort, insertion_sort, selection_sort, merge_sort]
# n_trial is a list of input sizes to be tested
n_trial = [100,250,500,750, 1000, 1250, 2500, 3750, 5000, 6250, 7500, 8750, 10000]
n_test = [100,250,500, 1000]

# trial is a data distionary used to create the columns for the pandas dataframe
# trial = {"size":sorts, "100":col_create(algorithms,100), "250":col_create(algorithms,250),"500":col_create(algorithms,500),"750":col_create(algorithms,750), "1000":col_create(algorithms,1000),"1250":col_create(algorithms,1250),"2500":col_create(algorithms,2500), "3750":col_create(algorithms,3750), "5000":col_create(algorithms,5000), "6250":col_create(algorithms,6250), "7500":col_create(algorithms,7500), "8750":col_create(algorithms,8750), "10000":col_create(algorithms,10000)}
test = {"size":sorts, "100":col_create(algorithms,100), "250":col_create(algorithms,250),"500":col_create(algorithms,500), "1000":col_create(algorithms,1000)}

# the main() function serves as a user interface for the application
def main():
  # the user can select one of 4 values
  allowed_modes = ["graph", "table", "export", "quit"]
  mode_chosen = input("How would you like to view the benchmark test? - graph/table/export/quit   ")
  # use a while loop to validate the data entered
  while mode_chosen not in allowed_modes:
    mode_chosen = input("How would you like to view the benchmark test? - graph/table/export/quit  ")
  # use a conditional to decide which fucntions to call
  # note that it recursively calls the main() function until the user chooses quit  
  if mode_chosen == "graph":
    results_plot(test, n_test, sorts)
    main()
  elif mode_chosen == "table":  
    print(df_create(test).to_string())
    main()
  elif mode_chosen == "export":
    results_export(test) 
    main() 
  else:
    quit()


# The program starts here by printing the splash screen
print('* * * * * * * * * * * * * * * * * * * * * * * * * * * * * * * * * * * * * * * *')          
print('*                                                                             *')
print('*                      Benchmarking Sorting Algorithms                        *')
print('*                                                                             *')
print('*              Written by Patrick Moore, GMIT, G00364753, 2019                *')
print('*                                                                             *')
print('* * * * * * * * * * * * * * * * * * * * * * * * * * * * * * * * * * * * * * * *')
main()