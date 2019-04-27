## Patrick Moore - GMIT - G00364753 - Comutational Thinking with Algorithms Project
# As this program takes a while to load - print a warning to the user
print("Please be patient while the program loads......")

# Section 1 - Import the required libraries for the project
import time
import numpy as np
import pandas as pd
import matplotlib.pyplot as plt

# Section 2 - Define the 5 Sorting Algorithms to be Used
# define the bubblesort algorithm - http://interactivepython.org/courselib/static/pythonds/SortSearch/TheInsertionSort.html
def bubble_sort(alist):
    # outer for loop runs from the last item in the list to the first in steps of 1
    for passnum in range(len(alist)-1,0,-1):
        # inner for loop runs from the start of the list to the current value of passnum
        for i in range(passnum):
            # if the current item is greater than the next one
            if alist[i]>alist[i+1]:
                # then switch them
                temp = alist[i]
                alist[i] = alist[i+1]
                alist[i+1] = temp
    return alist

# define the selection sort algorithm - http://interactivepython.org/runestone/static/pythonds/SortSearch/TheSelectionSort.html
def selection_sort(alist):
  # loop through the array from the last postion to the first
  for compare_element in range(len(alist)-1,0,-1):
    # set the position of max to 0
    positionOfMax=0
    # use a for loop to find the max value in the unsorted sub array 
    for location in range(1,compare_element+1):
      if alist[location]>alist[positionOfMax]:
        positionOfMax = location
    # swap the compared element with the max value from the sub array
    temp = alist[compare_element]
    alist[compare_element] = alist[positionOfMax]
    alist[positionOfMax] = temp
  return alist  

# define the insertion sort algorithm https://interactivepython.org/courselib/static/pythonds/SortSearch/TheInsertionSort.html
def insertion_sort(alist):
  # the outer for loop loops through the key values 
  # from the item at index 1 to the last item in the array
  for index in range(1,len(alist)):
    key = alist[index]
    position = index
    # this while loop finds the appropriate postion of each key value 
    # by searching through each item in the sorted array from the key postion index 1
    # or it will stop if it finds an item in the sorted list that is lower than the current key 
    while position>0 and alist[position-1]>key:
      # shift everything right one space 
      alist[position]=alist[position-1]
      # move onto the next item
      position = position-1
    # once the appropriate position is found the key is slotted into it  
    alist[position]=key
  # return the sorted list  
  return alist  

# define the merge sort algorithm - http://interactivepython.org/runestone/static/pythonds/SortSearch/TheMergeSort.html
def merge_sort(alist):
    # recursively split the list in half using mergesort
    # base case is when the lenght of the list is 1 or 0
    if len(alist)>1:
        mid = len(alist)//2
        lefthalf = alist[:mid]
        righthalf = alist[mid:]
        merge_sort(lefthalf)
        merge_sort(righthalf)
        # once the list is divided, merge it in correct order by checking each item in the sub arrays
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
    return alist        

# define the counting sort algorithm - https://www.w3resource.com/python-exercises/data-structures-and-algorithms/python-search-and-sorting-exercise-10.php
# note - this needs comments
def counting_sort(array1):
    # note that this is adapted code
    # i have hard coded 1000 in as the max value becase my array generator
    # creates lists of integers between 1 and 1000
    # create a counter array to count the number of instances of each number
    m = 1000 + 1
    count = [0] * m                
    for a in array1:
    # count occurences of each number in the array
        count[a] += 1             
    i = 0
    # recreate the array using information from the count step
    for a in range(m):            
        for c in range(count[a]):  
            array1[i] = a
            i += 1
    return array1

# Section 3 - Define the timer functions to benchmark the algorithms

# create a function to be used for generating the test arrays
def array_create(size):
  # return the array of the selected size
  return [np.random.randint(1000) for i in range(size)]

# define a function that takes an array and a sorting algorithm and times how long it takes to run
def timer(input_array,sort_algo):
  start = time.time()
  sort_algo(input_array)
  end = time.time()
  return (end-start)

# define a function to calucate the average running time of a sorting algorithm
def average_time(num_runs, size, sort_algo):
  # use an array to store the results of each trial
  trial_times = []
  # use a while loop to run the algorithm the specified number of times 
  counter = 0
  while counter < num_runs:
    input_array = array_create(size)
    trial_times.append(timer(input_array,sort_algo))
    counter = counter + 1
  # return the average time it takes to run the algorithm  
  return (sum(trial_times)/len(trial_times))

# Section 4 - Formatting the output

# create a function to carry out the trials
def algo_trial(algo, test_size):
  # this function takes an algorithm and test size and returns the average result of 10 trials in ms - formatted to 3 decimal places
  return float("{:10.3f}".format(average_time(10,test_size,algo)*1000))

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

# define a function that creates a pandas dataframe and plot the results based on the data dictionary,
# test input sizes and sorting algorithms passed to it
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
  # note the file name of the exported file is timestamped
  data.to_csv('benchmark' + str(time.ctime(int(time.time()))) + '.csv')

# Section 5 - User Interface

# create a list of the sorting algorithms to be tested
# 'sorts' is used to index the data frame
sorts = ['Bubble Sort', 'Insertion Sort', 'Selection Sort', 'Merge Sort', 'Counting Sort']
# 'algorithms' is a list of the function names
algorithms = [bubble_sort, insertion_sort, selection_sort, merge_sort, counting_sort]
# n_trial is a list of input sizes to be tested
n_trial = [100,250,500,750, 1000, 1250, 2500, 3750, 5000, 6250, 7500, 8750, 10000]
# trial is a data dictionary used to create the columns for the pandas dataframe
trial = {"size":sorts, "100":col_create(algorithms,100), "250":col_create(algorithms,250),"500":col_create(algorithms,500),"750":col_create(algorithms,750), "1000":col_create(algorithms,1000),"1250":col_create(algorithms,1250),"2500":col_create(algorithms,2500), "3750":col_create(algorithms,3750), "5000":col_create(algorithms,5000), "6250":col_create(algorithms,6250), "7500":col_create(algorithms,7500), "8750":col_create(algorithms,8750), "10000":col_create(algorithms,10000)}

# the main() function serves as a user interface for the application
def main():
  # the user can select one of 4 values
  allowed_modes = ["graph", "table", "export", "quit"]
  mode_chosen = input("How would you like to view the benchmark test? - graph/table/export/quit   ")
  # use a while loop to validate the user input
  while mode_chosen not in allowed_modes:
    mode_chosen = input("How would you like to view the benchmark test? - graph/table/export/quit  ")
  # use a conditional to decide which functions to call
  # note that it recursively calls the main() function until the user chooses quit  
  if mode_chosen == "graph":
    results_plot(trial, n_trial, sorts)
    main()
  elif mode_chosen == "table":  
    print(df_create(trial).to_string())
    main()
  elif mode_chosen == "export":
    results_export(trial) 
    print("Data exported to .csv")
    main() 
  else:
    quit()


# The program starts here by printing the splash screen and calling the main function
print('* * * * * * * * * * * * * * * * * * * * * * * * * * * * * * * * * * * * * * * *')          
print('*                                                                             *')
print('*                      Benchmarking Sorting Algorithms                        *')
print('*                                                                             *')
print('*              Written by Patrick Moore, GMIT, G00364753, 2019                *')
print('*                                                                             *')
print('* * * * * * * * * * * * * * * * * * * * * * * * * * * * * * * * * * * * * * * *')
main()