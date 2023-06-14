''' define a function which will test whether each row contains
exactly one of each int from 0-9'''
def rows(arr: list) -> bool:
    counter = 0
    valid = [1,2,3,4,5,6,7,8,9]
    for item in arr: 
        if sorted(item) != valid:
            return False
    return True



'''the same thing, but by forming columns
from the given data set'''
def columns(arr: list) -> bool:
    columns = []
    valid = [1,2,3,4,5,6,7,8,9]
    # counter = 0
    for x in range(0,9):
        c = [arr[y][x] for y in range(0,9)]
        columns.append(c)
    for c in columns:
        if sorted(c) != valid:
            return False
    return True

'''define a functon to generate the 
squares (9 of them) involved in a sudoku board,
and check that these are also only 0-9 and no
duplicates'''

def square_check(arr: list) -> bool:
    valid = [1,2,3,4,5,6,7,8,9]
    squares = []
    for x in range(3):
        for y in range(3):
            region = []
            for row in arr[x*3:(x+1)*3]:
                region +=  row[y*3:(y+1)*3]
                squares.append(region)
    if not rows(squares):
        return False
    else:
        return True
                    


'''this brings them all togehter into a single
 function which returns the output'''
def done_or_not(arr:list) -> str:
    if rows(arr) and columns(arr) and square_check(arr):
        print("nice")
        return True
    elif not rows(arr) or not columns(arr) or not square_check(arr):
        print("no")
        return True



# done_or_not([[1, 3, 2, 5, 7, 9, 4, 6, 8] 
#     ,[4, 9, 8, 2, 6, 1, 3, 7, 5] 
#     ,[7, 5, 6, 3, 8, 4, 2, 1, 9] 
#     ,[6, 4, 3, 1, 5, 8, 7, 9, 2] 
#     ,[5, 2, 1, 7, 9, 3, 8, 4, 6] 
#     ,[9, 8, 7, 4, 2, 6, 5, 3, 1] 
#     ,[2, 1, 4, 9, 3, 5, 6, 8, 7] 
#     ,[3, 6, 5, 8, 1, 7, 9, 2, 4] 
#     ,[8, 7, 9, 6, 4, 2, 1, 5, 3]])

# done_or_not([[1, 3, 2, 5, 7, 9, 4, 6, 8] 
#     ,[4, 9, 8, 2, 6, 1, 3, 7, 5]
#     ,[7, 5, 6, 3, 8, 4, 2, 1, 9]
#     ,[6, 4, 3, 1, 5, 8, 7, 9, 2]
#     ,[5, 2, 1, 7, 9, 3, 8, 4, 6]
#     ,[9, 8, 7, 4, 2, 6, 5, 3, 1]
#     ,[2, 1, 4, 9, 3, 5, 6, 8, 7]
#     ,[3, 6, 5, 8, 1, 7, 9, 2, 4]
#     ,[8, 7, 9, 6, 4, 2, 1, 3, 5]])

            