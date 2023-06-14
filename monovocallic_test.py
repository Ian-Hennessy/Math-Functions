

VOWELS = list('aeiou')

# definte a function to take a string and return a list
def get_word(word) -> list:
   return list(word)

# test viability of my word
def word_viability_test(word: str):
    return word.isalpha()

# filter consonants from test list
def filter_out_consonants(test: list) -> list:
    consonants = list('bcdfghjklmnpqrstvwxz')
    for letter in consonants:
        while letter in test:
            test.remove(letter)
    return test


# test the word for supervocallity
def test_word(test: list, VOWELS: list) -> bool:
    return sorted(test) == sorted(VOWELS)



if __name__ == '__main__':
    test = list(input("Please enter a word. \n"))
    length = int(len(test))
    # run the functions
    print(get_word(test))
    print(filter_out_consonants(test))
    print(word_viability_test(''.join(test)))
    print(test_word(test, VOWELS))
