


def sort_array(arr):
    ls = arr
    ls1 = arr.copy()
    oddlist = ls1
    for x in oddlist:
        if x % 2 == 0:
            oddlist.remove(x)
    for x in oddlist:
        if x == 0:
            oddlist.remove(0)
    oddlist.sort()
    oddlist = oddlist[::-1]

    evenlist = ls
    for x in evenlist:
        if x % 2 != 0:
            evenlist.insert(evenlist.index(x), ' ')
            evenlist.remove(x)
    print(evenlist)
    
    for x in evenlist:
        if x == ' ':
            index = int(evenlist.index(x))
            evenlist.insert(index, oddlist.pop())
            print(oddlist)
            evenlist.remove(x)
    return evenlist

# replace([5, 3, 2, 8, 1, 4])
replace()