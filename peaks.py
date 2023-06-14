
def find_next(arr: list) -> int:
    length = len(arr) - 1
    
    for i in range(0, length):
        if arr[i+1] != arr[i]:
            return int(arr[i+1])
            break
def plateau(arr: list) -> list:
    positions = []
    for i in range(1, len(arr) - 1):
        if arr[i] == arr[i+1] and arr[i] > arr[i-1]:
            next_int = find_next(arr[i:])
            if arr[i] > next_int:
                positions.append(i)
    return positions

def pick_peaks(arr: list) -> dict:
    maxes = {
    "pos": [],
    "peaks": []

    }
    for i in range(1,len(arr) - 1):
        if arr[i] == arr[i+1]:
            positions = plateau(arr)
            maxes["pos"] += positions
            for x in positions:
                maxes["peaks"] += [arr[x]]
    if len(arr) == 0:
        return maxes
    for i in range(1, len(arr) - 1):
        if arr[i] > arr[i-1] and arr[i] > arr[i+1]: 
            maxes["pos"] += [i]
            maxes["peaks"] += [arr[i]]
    maxes["pos"] = sorted(maxes["pos"])
    



            




    print(maxes)
    return maxes




# pick_peaks([3,2,3,6,4,1,2,3,2,1,2,2,2,1]) 
# '''3,7,10'''

# pick_peaks([1,2,5,4,3,2,3,6,4,1,2,3,3,4,5,3,2,1,2,3,5,5,4,3]) 
# '''2,7,14,20'''

pick_peaks([18, 18, 10, -3, -4, 15, 15, -1, 13, 17, 11, 4, 18, -4, 19, 4, 18, 10, -4, 8, 13, 9, 16, 18, 6, 7]) 
# '''5,9,12,14,16,20,23'''

# find_next([2,2,2,2,2,4])
# find_next([3,3,3,1])
# find_next([9,9,9,9,10])
# find_next([7,7,7,-3])

# pick_peaks([3,2,3,6,4,1,2,3,2,1,2,2,2,1])
# '''3,7,10'''
# '''6,3,2'''

# pick_peaks([2,1,3,1,2,2,2,2,1])
# '''2,4'''


pick_peaks([1,2,2,2,1,2,3,4,5,5,5,4])
# [1,8], [2,5]
