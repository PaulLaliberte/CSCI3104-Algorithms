#Insertion_sort

def insertionSort(array):
    j=2
    for j in range(len(array)):
        key = array[j]
        i=j-1
        while i>=0 and array[i] > key:
            array[i+1] = array[i]
            i = i-1
        array[i+1]=key


"""Testing"""

array=[3,5,2,1,4,6,123,453,10,56]
insertionSort(array)
print(array)


