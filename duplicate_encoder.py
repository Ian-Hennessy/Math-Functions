''' the purpose of this program is to encode a word by parsing for duplicates
and replacing those duplicates with '(' or ')' depending on 
how many times that letter appears. '''


def duplicate_encode(word):
    '''define lists and variables'''
    encoded = []
    new_list = []
    new_string = ''
    string_list = list(word)
    '''generate the new list with coded items'''
    for i in string_list:
        if string_list.count(i) == 1:
            encoded.append('(')
        else:
            encoded.append(')')
    '''generate a final string'''
    for x in encoded:
        new_string += f"{x}"
    return new_string


            




duplicate_encode('din')
duplicate_encode('wete')

