"""Partition with a three way split, < p, > p, == p."""

from partitionTest import *
import random

def swap(array, element1, element2):
    tmp = array[element1]
    array[element1] = array[element2]
    array[element2] = tmp


#---------------Partition----------------#

def lomutoTriple(a, l, r):
    pivot = a[r-1]             #pivot is the last element, by def. of lomuto
    i=0                        #set i=0, rather than i=-1
    k=r-1                      #k is the last index
    j=0                        #set j=0
        
    while j <= k:
        if a[j] < pivot:       #less than pivot -> swap, increment i,j up
            swap(a,i,j)
            i = i + 1
            j = j + 1
        elif a[j] is pivot:    #equal to pivot, leave in-place
            j = j + 1
        else:                  #greater than pivot -> swap, increment k down
            swap(a,j,k)
            k = k - 1
            
    return i               

#----------------------------------------#

def test(a):
    print('Input',a, 'Pivot:',a[len(a) -1])
    q = lomutoTriple(a, 0, len(a))
    isPartitioned(a, q)                           #Prof. Sriram's function
    print('Output',a)


t = 0
test_number = 3
while t < test_number:
    d = []
    for i in range(0,10):
        d.append(random.randint(0,10))
    
    print("Before partition: ", d, "\n")
    test(d)
    print("\n")
    t += 1

