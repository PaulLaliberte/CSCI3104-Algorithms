def _sort_3w(items, lo, hi):
    """
    Recursive sorting function with 3-way partitioning
    """
    lt = lo
    gt = hi
    pivot = items[lo]
    i = lo
    while i <= gt:
        if items[i] < pivot:
            items[lt], items[i] = items[i], items[lt]
            lt += 1
            i += 1
        elif items[i] > pivot:
            items[gt], items[i] = items[i], items[gt]
            gt -= 1
        else:
            i += 1


def test(a):
    print('Input',a, 'Pivot:',a[len(a) -1])
    q = _sort_3w(a, 0, len(a)-1)
    #isPartitioned(a, q)
    print('Output',a)


a = [10,5,9,11,12,4,5,2,1,5]

test(a)

