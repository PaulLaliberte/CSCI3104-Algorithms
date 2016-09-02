def checkIfCommonElement(array1, array2):
    i=0
    j=0

    while i < len(array1) and j < len(array2):
        if array1[i] is array2[j]:
            return True
        elif array1[i] < array2[j]:
            i = i + 1
        else:
            j = j + 1
    return False


#Tests
a = [3,5,456,23324]
b = [1,2,3,4]
c = [1,2,3,4,5]
d = [6,7,8,9,10]
print(checkIfCommonElement(a,b))
print(checkIfCommonElement(c,d))
