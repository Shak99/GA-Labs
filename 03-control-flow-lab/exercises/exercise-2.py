# exercise-02 Length of Phrase

# Write the code that:
# 1. Prompts the user to enter a phrase:
#      Please enter a word or phrase: 
word = input('Please enter a word or phrase:')
# 2. Print the following message:
#      - What you entered is xx characters long
while word != 'quit':
    print("What you entered is " + str(len(word)) + " characters long")
    word = input('Please enter a word or phrase:')
# 3. Return to step 1, unless the word 'quit' was entered.

