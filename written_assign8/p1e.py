"""Dynammic Programming, problem 1e"""


def LIS(a):
    """
    ******************
    Use of a memo table/list to find length
    ******************
    """

    l = len(a)
    memo_list = [1]*l

 
    for i in range (1 , l):
        for j in range(0 , i):
            if a[i] > a[j] and memo_list[i]< memo_list[j] + 1:
                memo_list[i] = memo_list[j]+1

        
    """
    *****************
    To find actual subseqeunce requires more work.
    *****************
    """

    subseqeunce = []

    for i in a:
        curr = i
        l_index = 0
        r_index = len(subseqeunce) - 1

        while l_index <= r_index:
            m = l_index + (r_index - l_index) // 2

            if subseqeunce[m] >= curr:
                r_index = m - 1
            else:
                l_index = m + 1

        if l_index == len(subseqeunce):
            subseqeunce.append(curr);
        else:
            subseqeunce[l_index] = curr

    return (max(memo_list), subseqeunce)
