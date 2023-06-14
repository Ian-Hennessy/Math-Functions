CONSONANTS = list('bcdfghjklmnpqrstvwxz')
test = list(input("Enter a string. \n"))
length = int(len(test))

# test viability of my word
def word_viability_test(test):
    for i in range(0, length):
        if int(test[i]) == True:
            raise TypeError("Please input a string.")

print(word_viability_test(test))