

from partitionTest import *


def swap(array, element1, element2):
    tmp = array[element1]
    array[element1] = array[element2]
    array[element2] = tmp
    print(array)



def partition(a, low, high):
    pivot = a[low]
    i = low
    j = high

    while i < j:

        while i < j and a[j] > pivot:
            if i < j:
                swap(a, i, j)
                i = i+1
            j = j -1

        while i < j and a[i] <= pivot:
            if i < j:
                swap(a, j, i)
                j = j-1
            i = i+1

    return i


"""
def quickS(a, low, high):
    q = tripleSort(a, low, high)
    quickS(a, low, q)
    quickS(a, q, high)

"""

def test(a):
    print('Input',a, 'Pivot:',a[len(a) -1])
    q = partition(a, 0, len(a)-1)
    isPartitioned(a, q)
    print('Output',a)




a = [12, 1, 5, 7, 15, 5]
test(a)
