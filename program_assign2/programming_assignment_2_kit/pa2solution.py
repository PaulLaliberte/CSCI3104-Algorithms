from __future__ import print_function
# in case you wish to use python2, but I strongly prefer that you use python3
import sys
import random

# NAME: Paul Laliberte'
# STUDENT ID NUMBER: 102312521
# On my honor as a University of Colorado Boulder student, I have not received any unauthorized help.
# I also realize that plagiarizing code defeats the purpose of an assignment like this and that the
# instructors and TAs have very sophisticated approaches to finding such plagiarism that can defeat
# things like renaming variables or rearranging statements.
#
# Acknowledged By: Paul Laliberte'


def free_time_intervals(interval_lst, T):
    missing = []
    interval_lst.sort()                                     #O(nlogn)
    x = 0
    if interval_lst[0][0] > x:
        missing.append((0, interval_lst[0][0]))             #1. check if start time missing
                                                            #O(1)
    y = interval_lst[0][1]
    i = 1

    for i in range(1, len(interval_lst)):                 #2. check internal times 
        if interval_lst[i][0] not in range(x,y+1):                       #O(n)
            if interval_lst[i][0] > T:
                missing.append((y, T))
            else:
                missing.append((y, interval_lst[i][0]))
                y = interval_lst[i][1]
        else:
            if interval_lst[i][1] > y:
                y = interval_lst[i][1]


    max_second_ele = 0
    for i in interval_lst:
        max_tuple = max(interval_lst, key=lambda x:x[1])
        max_second_ele = max_tuple[1]

    if max_second_ele < T:
        missing.append((y,T))

    missing.sort()                                          #O(nlogn)



    #Total Time: T(n) = 2O(nlogn) + O(n) + 2O(1)
    #                 = O(nlogn)



    return missing



def max_logged_in(interval_lst, T):
    max_time = []
    interval_lst.sort()
    count = 1
    x = interval_lst[0][0]
    y = interval_lst[0][1]
    time_int = x
    i = 1

    if len(interval_lst) > 1:
        for i in range(1, len(interval_lst)):
            if interval_lst[i][0] <= y and interval_lst[i][1] in range(x,y+1):
                count += 1
                if interval_lst[i][1] > x:
                    time_int = interval_lst[i][0]
            elif interval_lst[i][0] <= y and interval_lst[i][1] not in range(x, y+1) and interval_lst[i][0] == x:
                count += 1
                y = interval_lst[i][1]
            else:
                max_time.append((count, time_int))
                x = interval_lst[i][0]
                y = interval_lst[i][1]
                count = 1 
                time_int = x
    else:
        max_time.append((count, time_int))


    tup = max(max_time)

    return tup




if __name__ == '__main__':
    #Test Cases

    lst1 = [(5,15)]
    print('Input:', lst1)
    print(free_time_intervals(lst1,30))
    print(max_logged_in(lst1,30))

    lst2 = [(1,3), (2,8),(3,6), (2,6), (10,15), (12,17), (19,23), (27,35)]
    print('Input (corner-case):', lst2)
    print(free_time_intervals(lst2,30))
    print(max_logged_in(lst2,30))

    lst3 = [(5,15), (18,25), (3,12), (4, 11), (1,15), (18,19)]
    print('Input:', lst3)
    print(free_time_intervals(lst3,30))
    print(max_logged_in(lst3,30))
