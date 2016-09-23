from partitionTest import *


def swap(a,i,j):
    (a[i], a[j]) = (a[j], a[i])
    
def lomuto_partition(a, left, right):
    ''' Lomuto partition of array a from indices left to right-1. 
        Following Python convention, the left index is inclusive
        but right is not.'''
    n = len(a)
    assert( 0 <= left and left < right and right <= n )
    i = left - 1
    x = a[right -1]
    for j in range(left, right-1):
        if (a[j] <= x):
            swap(a, i + 1, j)
            i += 1
        # else nothing to do
    swap(a, i + 1, right -1 )
    return i + 1    
    
def test(a):
    print('Input',a, 'Pivot:',a[len(a) -1])
    q = lomuto_partition(a, 0, len(a))
    isPartitioned(a, q)
    print('Output',a)

a = [10, 9,11,12,4,2,1,5]
b = [70, 40, 80, 30, 90, 40]
c = [70,90, 80, 30, 90, 40, 90]

test(a)
test(b)
test(c)
