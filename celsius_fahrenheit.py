# Celsius to Fahrenheit
# Prompt the user for a number in degrees Celsius, and convert the value to degrees in Fahrenheit and display it to the user.
# Use the following formula:

# F = (C * 9/5) + 32
 

#create a variable with the value of an interger(nunber) along with the input of the deg in celsius 

temperature_in_celsius = int(input("Temperature in C? ")) 
# using the formula from above I solved the equaiton of 9/5 plus 32
temperature_in_fahrenheit = (temperature_in_celsius * 1.8) + 32

print(temperature_in_fahrenheit)
# this will then print the coversion into fahrenheit 



# Example Sessions: 
# $ python3 degree_conversion.py 
# Temperature in C? 28
# 82.4 F

# $ python3 degree_conversion.py
# Temperature in C? -5
# 23 F   ter
