"""Quick Sort"""

#import random
from partitionTest import *

def swap(array, element1, element2):
    tmp = array[element1]
    array[element1] = array[element2]
    array[element2] = tmp


#---------Partition----------#

def partition(a, l, r):
    # Implement Lomuto partition algorithm
    pivot=a[r-1] 
    i = l-1        
    for j in range(l,r-1):
        if (a[j] <= pivot):
            i = i+1
            swap(a,i,j)

    swap(a,i+1,r-1)
    return i+1

#---------------------------#

def test(a):
    print('Input',a, 'Pivot:',a[len(a) -1])
    q = partition(a, 0, len(a))
    isPartitioned(a, q)                           #Prof. Sriram's function
    print('Output',a)
    print("\n")


a = [10,5,1]
b = [70,40,80,30,90,40]           #duplicates on the left 
c = [54,26,22,17,77]

test(a)
test(b)
test(c)




"""

t = 0
test_number = 3
while t < test_number:
    d = []
    for i in range(0,20):
        d.append(random.randint(0,10))
    
    print("Before partition: ", d, "\n")
    test(d)
    print("\n\n")
    t += 1
"""


######## Duplicates on right of pivot ##########
