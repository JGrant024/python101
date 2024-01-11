# Tip Calculator

# Your task is to write a program that calculates how much of a tip to leave at a restaurant.

# Prompt the user for two things:

# The total bill amount
# The level of service, which can be one of the following: good, fair, or bad
# Calculate the tip amount and the total amount (bill amount + tip amount). The tip percentage based on the level of service is based on:

# good -> 20%
# fair -> 15%
# bad -> 10%

# Example session: 

# $ python3 tip_calc.py
# Total bill amount? 100
# Level of service? good
# Tip amount: $20.00
# Total amount: $120.00

# $ python3 tip_calc.py
# Total bill amount? 48
# Level of service? bad
# Tip amount: $4.80
# Total amount: $52.80


# Hints:

# Remember that you need to convert the input from the user input to floats instead of ints. Use the float function instead of the int function.
# To format a float number as a dollar value, use Python's formatting syntax: "%.2f" % amount






def count_tip(tip_amount, bill): 
    tip = bill * tip_amount
    total = bill + tip 
    return total

print(count_tip(.2, 100))
 