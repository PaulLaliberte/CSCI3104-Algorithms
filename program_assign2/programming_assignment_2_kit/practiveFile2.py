"""Practice file - problem 2"""


def max_logged_in(interval_lst, T):
    max_time = []
    interval_lst.sort()
    print(interval_lst)
    count = 1
    x = interval_lst[0][0]
    y = interval_lst[0][1]
    time_int = x
    i = 1

    if len(interval_lst) > 1:
        for i in range(1, len(interval_lst)):
            if interval_lst[i][0] <= y and interval_lst[i][1] in range(x,y+1):
                count += 1
                if interval_lst[i][1] >= y:
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
    #print(free_time_intervals(lst1,30))
    print(max_logged_in(lst1,30))
    print('\n')

    lst2 = [(1,3), (2,8),(3,6), (2,6), (10,15), (12,17), (19,23), (27,35)]
    print('Input (corner-case):', lst2)
    #print(free_time_intervals(lst2,30))
    print(max_logged_in(lst2,30))
    print('\n')

    lst3 = [(5,15), (18,25), (3,12), (4, 11), (1,15), (18,19)]
    print('Input:', lst3)
    #print(free_time_intervals(lst3,30))
    print(max_logged_in(lst3,30))
    print('\n')


   
