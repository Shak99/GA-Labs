# exercise-06 What's the  Season?

# Write the code that:
# 1. Prompts the user to enter the month (as three characters):
#      Enter the month of the year (Jan - Dec):
month = input('Enter the month of the year (Jan - Dec): ').upper()
# 2. Then prompts the user to enter the day of the month: 
#      Enter the day of the month:
day = input('Enter the day of the month: ')
# 3. Calculate what season it is based upon this chart:
#      Dec 21 - Mar 19: Winter
#      Mar 20 - Jun 20: Spring
#      Jun 21 - Sep 21: Summer
#      Sep 22 - Dec 20: Fall
# 4. Print the result as follows:
#      <Mmm> <dd> is in <season> 

if month in ('JAN', 'FEB', 'MAR'):
    if (month == 'MAR' and int(day) > 19):
        season = 'Spring'
    else:
        season = 'Winter'

if month in ('APR', 'MAY', 'JUN'):
    if (month == 'JUN' and int(day) > 20):
        season = 'Summer'
    else:
        season = 'Spring'

if month in ('JUL', 'AUG', 'SEP'):
    if (month == 'SEP' and int(day) > 21):
        season = 'Fall'
    else:
        season = 'Summer'

if month in ('OCT', 'NOV', 'DEC'):
    if (month == 'DEC' and int(day) > 20):
        season = 'Winter'
    else:
        season = 'Fall'
        
print(f"{month} {day} is in {season}")

# Hints:
# Consider using the in operator to check if a string is in a particular list/tuple like this:
# if input_month in ('Jan', 'Feb', 'Mar'):
#
# After setting the likely season, you can use another if...elif...else statement to "adjust" if
# the day number falls within a certain range.