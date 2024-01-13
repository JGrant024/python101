# 4.) Day of the Week 

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

# here we declare our variables using the given format and placing days of the week in a list that can be indexed. 
day = int(input("day(0-6)?"))
day_of_week = ["Monday", "Tuesday", "Wednesday", "Thursday", "Friday", "Saturday", "Sunday"]

# created a if else statement for collet inputs between 0-6 

if 0 <= day <= 6: 
    print(day_of_week[day])
else:
    print("Oops! Please enter a number between 0 and 6.")