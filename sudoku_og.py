
'''this is my original solution. it has since been optimized 
by studying others' code'''


''' define a function which will test whether each row contains
exactly one of each int from 0-9'''
def rows(arr: list) -> bool:
    counter = 0
    for item in arr: 
        for x in item:
            if x == 0:
                return False
            if item.count(x) > 1:
                return False
                break
            elif item.count(x) == 1:
                counter += 1
    '''count should be 9^2 if all
     data points add +1 and the square is 
    9x9'''
    if counter == 81:
        return True




'''the same thing, but by forming columns
from the given data set'''
def columns(arr: list) -> bool:
    columns = []
    counter = 0
    for x in range(0,9):
        c = [arr[y][x] for y in range(0,9)]
        columns.append(c)
    for c in columns:
        for x in c:
            if c.count(x) > 1:
                return False
                break
            elif c.count(x) == 1:
                counter += 1
    '''count should be 9^2 if all 
    data points add +1 and the square is 
    9x9'''
    if counter == 81:
        return True

'''define a functon to generate the 
squares (9 of them) involved in a sudoku board,
and check that these are also only 0-9 and no
duplicates'''

def square_check(arr: list) -> bool:
    sq1 = []
    sq2 = []
    sq3 = []
    sq4 = []
    sq5 = []
    sq6 = []
    sq7 = []
    sq8 = []
    sq9 = []
    squares = [sq1, sq2, sq3,
    sq4, sq5, sq6,
    sq7, sq8, sq9]
    for x in arr[:3]:
        for i in x[:3]:
            sq1.append(i)
        for i in x[3:6]:
            sq2.append(i)
        for i in x[6:9]:
            sq3.append(i)
   
    for x in arr[3:6]:
        for i in x[:3]:
            sq4.append(i)
        for i in x[3:6]:
            sq5.append(i)
        for i in x[6:9]:
            sq6.append(i) 
   
    for x in arr[6:9]:
        for i in x[:3]:
            sq7.append(i)
        for i in x[3:6]:
            sq8.append(i)
        for i in x[6:9]:
            sq9.append(i)
    if not rows(squares):
        return(False)
    else:
        return True






'''this brings them all togehter into a single
 function which returns the output'''
def valid_solution(arr:list) -> str:
    if rows(arr) and columns(arr) and square_check(arr):
        return True
    elif not rows(arr) or not columns(arr) or not square_check(arr):
        return False