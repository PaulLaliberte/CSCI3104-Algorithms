"""Problem2, A and B"""


def p2A(array, T):
    dic = {}
    for i in array:
        dic[i] = i

    for j in array:
        find_value = T - j
        if find_value in dic:
            return (j, dic[find_value])


def p2B(array, T, itr=0):
    try:
        find_value = T - array[itr]
        x = p2A(array, find_value)
        if x is not None:
            print((x[0], x[1], array[itr]))
        else:
            itr += 1
            p2B(array, T, itr)
    except IndexError:
        #no solution
        print("No Solution.")
    


