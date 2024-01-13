# Prompt the user for the missing words to a Madlib sentence using 
# the input function. You can make up your own Madlib sentence, 
# but here's an example:

# ____(name)____'s favorite subject in school is ____(subject)____.

# $ python3 madlib.py
# Please fill in the blanks below:
# ____(name)____'s favorite subject in school is ____(subject)____.
# What is your name? Marty
# What is your favorite subject? time travel
# Marty's favorite subject in school is time travel.


name = input("What is your name? ")
subject = input("What is your favorite subject? ")
print("%s's favorite subject in school is %s." % (name, subject))
