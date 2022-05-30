import copy
import os.path
import pathlib
import random

# Name: Ethan Janovitz
# Assignment: Searching and Sorting algorithms
# Stage 4 Language Project


def write_file():
    i = 0
    # Opening file to write in the data, "w" allows us to write into the file
    file = open("testFile1.txt", "w")

    # loop to add random numbers to the file - runs 200,000
    while i <= 200000:
        if i == 200000:
            # the str() is here to convert the random number to a string
            # can't really compare this to java since the files were given to us
            file.write(str(random.randrange(0, 500000)))
        else:
            file.write(str(random.randrange(0, 500000)))
            file.write(str(", "))

        i = i + 1

    # closes the file, the code in java is the same
    file.close()

# try block is very similar to java's try block instead
# of catch python uses except, and they work exactly the same
try:
    # this line creates the file
    # "testFile1.txt" -> names the file and tells you what type of file it is
    # "w" -> means write in the file, there are many other options
    # for example "a" is appending stuff to the file so it will add on to what ever is there
    # and "r" is reading whats in the file
    file = pathlib.Path("testFile1.txt", "w")
    if file.exists():
        print("This file exists")

except FileNotFoundError:
    print("THIS FILE DOES NOT EXIST")
    write_file()

# Reading in file
with open("testFile1.txt", 'r') as file:
    data = file.read()

# List comprehension
# Split the data file at ", " and for each item
# of data save as and integer of x to the variable
# data_list. This is similar to the while loop in java
# that iterates through the data file and adds each item
# of data to a new array
data_list = [int(x) for x in data.split(", ")]

print(len(data_list) - 1)


# bubble sort function, just like in java we need to send the function the list,
# so it has access and can sort the list
def bubble_sort(data):
    print("RUNNING SORT")

    # the for loop is typed differently compared to the for loop in java
    # but they both do the exact same thing
    # len(data) is grabbing the length of the list, in java the code
    # would be typed as data.length, which is sort of similar
    # the range() starts at 0 by default and increments by 1 by default
    # java's version of range() would be the in this example x++ and i++
    # which is just where x and i are adding one to themselves
    for x in range(len(data) - 1):
        for i in range(len(data) - 1):
            # if statement is the exact same in java
            if data[i] > data[i + 1]:
                # this part of the code is swapping elements in the list
                # in my option this is a lot cleaner than in java
                # the code to complete this task in java was(this is how I did it)
                #             int temp = tempNums[min];
                #             tempNums[min] = tempNums[i];
                #             tempNums[i] = temp;
                # as you can see a temp variable had to be created to achieve what we
                # wanted but in python there is no need for this
                data[i], data[i + 1] = data[i + 1], data[i]
    print("FINISHED SORT")
    return data


# The code for the selection sort in python compared to java
# is practically the same just a for loop in a for loop
# all the differences ive already explained in the bubble sort algorithm
def selection_sort(data):
    print("RUNNING SELECTION SORT")
    for i in range(len(data)):

        minimun = i
        for j in range(i + 1, len(data)):
            if data[j] < data[minimun]:
                minimun = j

        data[i], data[minimun] = data[minimun], data[i]

    print("FINISHED SORT")
    return data


# The code for the insertion sort in python compared to java
# is practically the same just a for loop in a while loop
def insertion_sort(data):
    print("RUNNING INSERTION SORT")
    for i in range(len(data)):
        tracker = data[i]
        j = i - 1

        # instead of using && in java, python you are allowed to actually just
        # type and
        while j >= 0 and data[j] > tracker:
            data[j + 1] = data[j]
            j = j - 1

        data[j + 1] = tracker

    print("FINISHED SORT")
    return data


# the binary search is very similar to java once again
def binary_search(data):
    print("RUNNING SEARCH")

    # all the variables are the same
    lower = 0
    upper = len(data) - 1

    # in this line I had to wrap the calculation in and "int()" to convert it into an integer
    # if the "int()" isn't there then an error occurs
    currently_selected = int((upper + lower) / 2)
    target = 356

    while upper >= lower:

        if data[currently_selected] < target:
            lower = currently_selected + 1
        elif data[currently_selected] > target:
            upper = currently_selected - 1
        else:
            return currently_selected

        # in this line I had to wrap the calculation in and "int()" to convert it into an integer
        # if the "int()" isn't there then an error occurs
        currently_selected = int((upper + lower) / 2)

        if upper < lower:
            currently_selected = -1
    print("FINISHED SEARCH")
    return currently_selected


# creates a clone of the unsorted list so when it gets to the next sorting algorithm
# it's not sorting an already sorted list
# in java the code would just be written as int[] unsorted_list = data_list.clone()
# there are many ways to copy/clone a list in python, and they are very easily done
unsorted_list = copy.copy(data_list)
bubble_sort(unsorted_list)
unsorted_list = copy.copy(data_list)
selection_sort(unsorted_list)
unsorted_list = copy.copy(data_list)
insertion_sort(unsorted_list)

# JUST FOR TESTING PURPOSES AND TO MAKE THE CONSOLE LOOK A BIT CLEANER
print("-----------------------------------------")
print("-----------------DIVIDER-----------------")
print("-----------------------------------------")

print(binary_search(unsorted_list))
