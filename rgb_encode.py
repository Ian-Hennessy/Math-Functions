def rgb(r, g, b):
    initial = [r,g,b]
    hexstring = ''
    '''define hex for values more than 10'''
    alphabet = {
    10:'A',
    11:'B',
    12:'C',
    13:'D',
    14:'E',
    15:'F'
    }
    '''alter out-of-bounds numbers'''
    for x in initial:
        if x < 0:
            initial.insert(initial.index(x), 0)
            initial.remove(x)
        elif x > 255:
            initial.insert(initial.index(x), 255)
            initial.remove(x)
    '''generate the hex'''
    hexlist = []
    for x in initial:
        a = x%16
        b = (x-a)/16
        if b >= 10:
            b = alphabet[b]

        if a >= 10:
            a = alphabet[a]

        if type(b) == float or type(b) == int:
            b = int(b)
        if type(a) == float or type(a) == int:
            a = int(a)
        hexlist.append(b)
        hexlist.append(a)
    for x in hexlist:
        hexstring += f'{x}'

    return hexstring



