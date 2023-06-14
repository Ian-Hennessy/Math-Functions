''' this is a code wars exercise that wants me to take an 
array of ints and return a phone number in the form 
(xxx) - xxx - xxxx'''

def phone_number(array) -> str:
    number = ['(', ')', '-', '-']
    indexes = 10
    for index in range(0,3):
        number.insert(index+1, array[index])

    for index in range(3,6):
        number.insert(index+3, array[index])

    for index in range(6,10):
        number.insert(index+5, array[index])

    return number.join()








phone_number([8,0,8,2,8,2,8,0,2,7])