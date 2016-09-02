def findCommonElement(array1, array2):
    i=0
    j=0
    count = 0
    
    while i < len(array1) and j < len(array2):
        if array1[i] < array2[j]:
            i = i + 1
        elif array1[i] is array2[j]:
            print("The number %i is common." % array1[i])
            i = i + 1
            j = j + 1
            count = count + 1
        else:
            mergedArray.append(array2[j])
            j = j + 1
    print("Number of common elements is: %i" % count)

"""
    while i < len(array1):
        mergedArray.append(array1[i])
        i = i + 1

    while j < len(array2):
        mergedArray.append(array2[j])
        j = j + 1


    return mergedArray
"""


