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

tip_percentage = " "
good = 20
fair = 15 
bad = 10

total_bill = float(input("Total bill amount? "))
level_of_service = input("Level of service? ") .lower() 

if level_of_service == "good": 
    tip_percentage = good 
elif level_of_service == "fair": 
    tip_percentage = fair 
elif level_of_service == "bad": 
    tip_percentage = bad 
else: 
    print("Opps! Invalid service level. Please enter good, fair, or bad.")
    exit() 

tip_amount = total_bill * (tip_percentage / 100) 
total_amount = total_bill + tip_amount

print(f"Tip amount: ${tip_amount:.2f}")
print(f"Total amount: ${total_amount:.2f}")


