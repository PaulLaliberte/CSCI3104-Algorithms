"""Practice file for program assignment 2"""

def free_time_intervals(interval_lst, T):
    missing = []
    interval_lst.sort()                                     #O(nlogn)
    print(interval_lst)
    x = 0                   
    if interval_lst[0][0] > x:
        missing.append((0, interval_lst[0][0]))             #1. check if start time missing
                                                            #O(1)
    y = interval_lst[0][1]
    i = 1

    for i in range(1, len(interval_lst)):                 #2. check internal times 
        if interval_lst[i][0] not in range(x,y+1):                       #O(n)
            missing.append((y, interval_lst[i][0]))
            y = interval_lst[i][1]
        else:
            if interval_lst[i][1] > y:
                y = interval_lst[i][1]

    l = len(interval_lst) - 1                               #3. check if end time missing
    y = interval_lst[l][1]                                             #O(1)
    if y < T:
        missing.append((y,T))

    missing.sort()                                          #O(nlogn)



    #Total Time: T(n) = 2O(nlogn) + O(n) + 2O(1)
    #                 = O(nlogn)



    return missing

if __name__ == '__main__':
    #Test Cases

    lst1 = [(5,15)]
    print('Input:', lst1)
    print(free_time_intervals(lst1,30))
    #print(max_logged_in(lst1,30))
    print('\n')

    lst2 = [(1,3), (2,8),(3,6), (2,6), (10,15), (12,17), (19,23), (27,35)]
    print('Input (corner-case):', lst2)
    print(free_time_intervals(lst2,30))
    #print(max_logged_in(lst2,30))
    print('\n')

    lst3 = [(5,15), (18,25), (3,12), (4, 11), (1,15), (18,19)]
    print('Input:', lst3)
    print(free_time_intervals(lst3,30))
    #print(max_logged_in(lst3,30))
    print('\n')

    
    
