def last_resort(parenlist):
    '''stack to pop on and off of'''
    stack = []
    for x in parenlist:
        if x =='(':
            stack.append(x)
        if x == ')' and len(stack) > 0:
            stack.pop()
        elif x == ')' and len(stack) == 0:
            print(False)
            return False

    if len(stack) == 0: 
        print(True)
        return True

    else:
        print(False)



def valid_parentheses(string):

    ls = list(string)
    '''clear alphanumeric chars'''
    strlist = [i for i in ls if not i.isalnum()]
    
    # no items is true
    if len(strlist) == 0:
        print(True)
        return True
    if len(strlist) == 1:
        return False
        
    # can't start with ')' and be true
    elif strlist[0] == ')':
        print(False)
        return False

    # must have the same amount of '(' and ')'
    elif strlist.count('(') != strlist.count(')'):
        print(False)
        return False

        
    # check if the last item is '('
    elif strlist[len(strlist) - 1] == '(':
        print(False)
        return False

    else:
        last_resort(strlist)



valid_parentheses("hi(hi)()") #True
