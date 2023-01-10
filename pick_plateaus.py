def find_next(arr: list) -> int:
    length = len(arr) - 1
    
    for i in range(0, length):
        if arr[i+1] != arr[i]:
            print(int(arr[i+1]))
            return int(arr[i+1])
            break

def plateau(arr: list) -> list:
    positions = []
    for i in range(0, len(arr) - 1):
        if arr[i] == arr[i+1] and arr[i] > arr[i-1]:
            next_int = find_next(arr[i:])
            if arr[i] > next_int:
                positions.append(i)
    return positions



plateau([1,2,2,2,1,2,3,3,3,3,3,2])

