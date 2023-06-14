
# Python Scoping Rules: 
# Local
# Enclosing
# Global
# Builtin

vowels = set('aeiou')
all_lowercase_word = word.lower()
return all_lowercase_word[0] in vowels 


# TODO: finish this stub
def starts_with_vowel(word: str) -> bool:
    """Takes a word and determines if the first letter is a vowel"""
    # ...
    return first_letter_is_vowel

# def vowel_test():
#     global vowel_Bool
#     vowel_Bool = False
#     # ask for the word being used
#     word = input("What word are you testing?")
#     # split the word into separate characters
#     word_list = [*word]
#     first_letter = word_list[0]
#     print(f"{first_letter}")
#     vowels_list = ["a", "e", "i", "o", "u", "A", "E", "I", "O", "U"] # list('aeiouAEIOU')
#    # cross-reference first letter with the list of vowels.
#     for vowel in vowels_list:
#         if first_letter == vowel:
#             vowel_Bool = True

