# 4.) Day of ther Week 

# Given the following code that prompts the user for a day number
#  (Remember that the int function converts a numeric string to a
#  number):


# day = int(input("day(0-6)?"))
#Fill in your code here 

# The user will enter a number from 0 to 6. Given this number, 
# print a day of the week. 0 for Sunday, 1 for Monday, 2 for 
# Tuesday, and so on. Here's an example user session (this assumes you've named the file day_of_week.py):

# $ python3 day_of_week.py
# Day (0-6)? 5
# Friday
# $ python day_of_week.py
# Day (0-6)? 0
# Sunday

day = int(input('Day (0-6)? '))

week_day = ''

if day == 0:
  week_day = 'Sunday'
if day == 1:
  week_day = 'Monday'
if day == 2:
  week_day = 'Tuesday'
if day == 3:
  week_day = 'Wednesday'
if day == 4:
  week_day = 'Thursday'
if day == 5:
  week_day = 'Friday'
if day == 6:
  week_day = 'Saturday'

print(week_day)