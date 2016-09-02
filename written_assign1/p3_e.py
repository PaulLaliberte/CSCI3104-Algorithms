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
a = [1,2,500,12312,2123,22,3]
b = [10,12320,450, 2321]
print(maximumProfit(a))
print(maximumProfit(b))
