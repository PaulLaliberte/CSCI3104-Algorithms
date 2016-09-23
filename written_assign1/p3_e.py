"""Find maximumprofit in < O(n) time"""

def maximumProfit(array):
    maximum = 0

    for i in range(len(array)):
        if maximum < array[i]:
            maximum = array[i]

    minimum = maximum 

    for j in range(len(array)):
        if minimum > array[j]:
            minimum = array[j]

    return maximum - minimum



#Tests
a = [1,4,6,7,3,1]
b = [100,23,1123,678,45,987]
c = [1000, 23, 445, 987, 0, 1, 123]
d = [2324, 3000, 4, 9, 123]
print(maximumProfit(a))
print(maximumProfit(b))
print(maximumProfit(c))
print(maximumProfit(d))
