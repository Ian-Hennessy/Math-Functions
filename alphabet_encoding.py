# generate a dictionary for the alphabet
alphabet = {
    'a':1, 
    'b':2,
    'c':3,
    'd':4,
    'e':5,
    'f':6,
    'g':7,
    'h':8,
    'i':9,
    'j':10,
    'k':11,
    'l':12,
    'm':13,
    'n':14,
    'o':15,
    'p':16,
    'q':17,
    'r':18,
    's':19,
    't':20,
    'u':21,
    'v':22,
    'w':23,
    'x':24,
    'y':25,
    'z':26


}


def alphabet_position(string): 
    new_string = string.lower()
    alpha_list = list(new_string)
    alphanum_str = ''
    for letter in new_string:
        # check if letter
        if letter.isalpha():
            #generate a string for the new alphanumeric replacements
            alphanum_str += f'{alphabet[letter]} '
    # return the answer without the extraneous space
    return alphanum_str[:-1]