"""
You are given an array of n positive numbers. 
Find the smallest positive number that is missing in the array.
If all elements from 1 to n are present, then the smallest missing number is n+1.

Your algorithm should run in linear time, ie O(n), given the size of the array n.
You are not allowed to use extra arrays or hashtables. You may however rearrange the elements in the input array.
"""


#Sort the list, find the first missing value, i.e. the smallest
#If no missing values, return n+1 (j+1 in my algo)
#
#Time Complexity: 
#    not O(n), nested for loop... O(n^2)

def sortArray(array):
    length = len(array)
    for i in range(length):
        if (i + 1 <= length-1) and array[i] > array[i+1]:
            array[i], array[i+1] = array[i+1], array[i]


def completeSort(array):
    for i in range(len(array)):
        sortArray(array)


def findMissing(array):
    missing = 0
    j = 1
    for i in array:
        if i == j:
            missing = 0
            j = j+1
        elif i > j:
            missing = j
            break
    if missing == 0:
        return(len(array) + 1)
    else:
        return(missing)





#Tests
arr = [1]
arr1 = [1,6,2,5,4]
arr2 = [1,2,3,4,5]
arr3 = [1,342,10283,3,1221,1000000]


sortArray(arr3)
completeSort(arr3)
print(findMissing(arr3))
