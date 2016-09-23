"""Binary search algorithm for finding "peaked" element"""


def recursiveFindMax(array, left, right):
    mid = (left+right)/2
    if array[int(mid)] > array[int(mid-1)] and array[int(mid)] > array[int(mid+1)]:
        return array[int(mid)]
    elif array[int(mid)] > array[int(mid-1)] and array[int(mid)] < array[int(mid+1)]:
        return recursiveFindMax(array,mid+1,right)
    else:
        return recursiveFindMax(array,left,mid-1)


#Tests
a = [1,2,3,5,4,1]
b = [1,2,5,17,19,15,12,11,4,2,1,0]
c = [1,5,123,10342,1000000,99,4,2]
d = [1,7,3]

print(recursiveFindMax(a, 0, len(a)-1))
print(recursiveFindMax(b, 0, len(b)-1))
print(recursiveFindMax(c, 0, len(c)-1))
print(recursiveFindMax(d, 0, len(d)-1))

