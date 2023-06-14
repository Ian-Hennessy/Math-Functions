import math


def standard_deviation(arr: list[int]) -> float:
    # generate initial summation to calculate average
    summation = sum(arr)
    average = summation/(int(len(arr)))
    print(average)
# new list of x - x_ave
    new_arr = []
    for x in arr: 
        new_arr.append(x-average)
    final_sum = sum(new_arr)
    # summation of x - x_ave
    if final_sum > 0:
        stdev = math.sqrt(final_sum/(len(arr)))
    elif final_sum < 0:
        stdev = math.sqrt((-1) * final_sum/len(arr))
    elif final_sum == 0:
        stdev = 0

    print(stdev)


# arr6 = [339, 281, 336, 383, 369]

# arr12 = [675, 669, 669, 669, 675]

# arr18 = [965, 964, 965, 965 ,964, 965]

# arr24 = [1329, 1327, 1708, 1626, 1326]

# arr30 = [1683, 1674, 1674, 1701, 1683]

# standard_deviation(arr6)
# standard_deviation(arr12)
# standard_deviation(arr18)
# standard_deviation(arr24)
# standard_deviation(arr30)


arrTare = []

arr150= []

# arrWeight = [
# 1.197,
# 1.145,
# 1.252,
# 1.273,
# 1.177]

standard_deviation(arrTARE)
standard_deviation(arr150)