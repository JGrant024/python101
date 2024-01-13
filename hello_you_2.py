# HELLO YOU Same as the first exercise, but this time print the user's name in ALL CAPS, and also tell them the number of letters in their name.

# (Hint: You'll want to search for documentation on how to uppercase a string.)

# Example session: $ python3 hello2.py
# WHAT IS YOUR NAME? Alice
# HELLO, ALICE!
# YOUR NAME HAS 5 LETTERS IN IT! AWESOME!



name = input("What is your name? ")
name_uppercase = name.upper() 
expression = "your name has 5 letters in it! awesome!"
expression_uppercase = expression.upper()
print("HELLO, " + name_uppercase + "!") 
print(expression_uppercase)



