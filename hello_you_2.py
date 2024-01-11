# HELLO YOU Same as the first exercise, but this time print the user's name in ALL CAPS, and also tell them the number of letters in their name.

# (Hint: You'll want to search for documentation on how to uppercase a string.)

# Example session: $ python3 hello2.py
# WHAT IS YOUR NAME? Alice
# HELLO, ALICE!
# YOUR NAME HAS 5 LETTERS IN IT! AWESOME!





question = input("What is your name? ")
uppercase_name = question.upper()

greeting = "Hello, " + uppercase_name + "!"
print(greeting)

name_length = len(question)
response = "Your name has " + str(name_length) + " letters in it! Awesome!"
print(response.upper())


# What is your name is not accpetiing the upper function. Research on this later. 
