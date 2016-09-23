def isPartitioned(a, j, verbose=True):
    # Check that the array a is properly partitioned at position j
    n = len(a)
    assert ( j >= 0 and j < n) # otherwise this makes no sense to 
                               # say array a is partitioned at j
    fail = False
    x = a[j] # the value of the pivot
    if verbose:
        print('The pivot is:', x)
    # Check all elements before the pivot
    for k in range(0, j): # recall range in python runs from 0 to j-1
        if (a[k] > x):
            if (verbose):
                print( 'Partition fails at position: a[%d] =  %d'%(k, a[k]) )
            fail = True
    for k in range(j+1, n):
        if (a[k] < x):
            if (verbose):
                print('Partition fails at position a[%d] = %d'%(k, a[k]))
            fail = True
    if verbose:
        if (not fail):
            print('-> Partition is correct (trumpets please)')
        else:
            print('-> Partitioned failed (wawa trombones please)')
    return (not fail)
