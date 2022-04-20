# exercise-01 Vowel or Consonant

# Write the code that:
# 1. Prompts the user to enter a letter in the alphabet:
#      Please enter a letter from the alphabet (a-z or A-Z): 
letter = input('Please enter a letter from the alphabet (a-z or A-Z):').lower()
# 2. Write the code that determines whether the letter entered is a vowel
vowels = ['a', 'e', 'i', 'o', 'u']
# 3. Print one of following messages (substituting the letter for x):
#      - The letter x is a vowel
#      - The letter x is a consonant

def checkVowel(abc):
    isTrue = False
    for x in vowels:
        if abc == x:
            isTrue = True
    return isTrue
                 
if checkVowel(letter) == True:
    print("The letter x is a vowel")
else:
    print("The letter x is a consonant")

# Hints:  Use the in operator to check if a character is in another string
#         For example, if some_char in 'abc':