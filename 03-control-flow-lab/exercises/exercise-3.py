# exercise-03 Calculate Dog Years

# Write the code that:
# 1. Prompts the user to enter a dog's age in human years like this:
#      Input a dog's age in human years: 
dogAge = input("Input a dog's age in human years: ")
# 2. Calculates the equivalent dog years, where:
#      - The first two years count as 10 years each
#      - Any remaining years count as 7 years each
age = 0
dogAge = int(dogAge)
if(dogAge >= 2):
    age += (10*2)
    dogAge -= 2
    age += (dogAge*7)
else:
    age = dogAge * 7

# 3. Prints the answer in the following format:
#      The dog's age in dog years is xx

print(f"The dog's age in dog years is {age}")

# Hint:  Use the int() function to convert the string returned from input() into an integer