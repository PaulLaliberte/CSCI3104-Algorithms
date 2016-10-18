"""Problem 5"""

def beforeSort(a):
    #convert input to tuples
    b = []
    i = 0
    while i < len(a):
        h = i+1
        if h > len(a)-1:
            b.append((a[i], None))       #if past end, place None
            break
        else:
            if a[i] > a[h]:              #if i+1 > i switch append
                b.append((a[h], a[i]))   #places
                i = i+2
            else:
                b.append((a[i],a[h]))
                i = i+2
    return b

def afterSort(a):
    c = []
    for i in a:
        for j in i:
            if j is None:
                pass
            else:
                c.append(j)
    return c


if __name__=="__main__":
    a = ["paul lali", "paul johnson", "captain blackbeard"]
    b = ["jimmy john", "jimmy apple", "jimmy zane"]
    c = ["tori yuo", "tori xu", "jeff aladdin"]
    print("Input: ", a, "\n")
    print("Modifing input before sort: \n")
    h = beforeSort(a)
    print(h, "\n")
    print("Sorting with python sort: ")
    h.sort()
    print(h, "\n")
    print("Modifing input back: \n")
    n = afterSort(h)
    print(n, "\n")

    print("\n\n")

    print("Input: ", b, "\n")
    print("Modifing input before sort: \n")
    h = beforeSort(b)
    print(h, "\n")
    print("Sorting with python sort: ")
    h.sort()
    print(h, "\n")
    print("Modifing input back: \n")
    n = afterSort(h)
    print(n, "\n")

    print("\n\n")

    print("Input: ", c, "\n")
    print("Modifing input before sort: \n")
    h = beforeSort(c)
    print(h, "\n")
    print("Sorting with python sort: ")
    h.sort()
    print(h, "\n")
    print("Modifing input back: \n")
    n = afterSort(h)
    print(n, "\n")


