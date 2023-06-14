def median_sort(ls1: list, ls2: list) -> float:
    concat = [*ls1, *ls2]

    sort = sorted(concat)

# Testcase for when the new list is of length such that length % 2 == 0, even number
    if len(sort) % 2 == 0:
        mid1 = sort[int(len(sort)/2)-1] 
        # print(mid1)
        mid2 = sort[int(len(sort)/2)] 
        # print(mid2)
        median = (mid1 + mid2)/2


# Testcase for when the new list is of odd length
    elif len(sort) % 2 != 0:
        middle = int(len(sort)/2)
        median = sort[middle]
    

    print(median)
    return median



median_sort([1,2],[2])

median_sort([1,2], [3,4])