def solution(string):
    list_1 = list(string)
    # if the list isn't an even number of items, add a '_'
    if len(list_1) % 2 != 0:
        list_1.append('_')
    # create an empty list for new entires
    list_2 = []
    # turn items in list 1 into new pairs
    for num in range (0, len(list_1)):
        if num % 2 == 0:
            pair = f"{list_1[num]}{list_1[num+1]}"
            list_2.append(pair)
    return list_2

