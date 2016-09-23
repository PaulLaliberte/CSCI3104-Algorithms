def findMinimum(array, left, right):
    b = []
    array = array[left:right]
    for i in range(len(array)):
        if len(b) is 0:
            b.append(array[i])
        else:
            if b[0] > array[i]:
                b[0] = array[i]
    return b[0]


def findMaximumProfit(array):
    c = []
    for i in range(len(array)):
        if len(c) is 0:
            c.append(array[i])
        else:
            if c[0] < array[i]:
                c[0] = array[i]

    return c[0] - findMinimum(array,0,len(array)-1)



#Tests
a = [1,4,6,7,3,1]
b = [100,23,1123,678,45,987]
c = [1000, 23, 445, 987, 0, 1, 123]
d = [2324, 3000, 4, 9, 123]
print(findMinimum(a,0,5))
print(findMinimum(b,1,5))
print(findMinimum(c,0,6))
print(findMinimum(d,0,4))
print("\n")
print("Finding maximum profit")
print(findMaximumProfit(a))
print(findMaximumProfit(b))
print(findMaximumProfit(c))
print(findMaximumProfit(d))






