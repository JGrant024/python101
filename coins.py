# Write a program that will prompt you for how many coins you want. 
# Initially you have no coins. It will ask you if you want a coin? If you type "yes", 
# it will give you one coin, and print out the current tally. If you type no, it will 
# stop the program. 
# Example run:$ python3 coins.py



# You have 0 coins.
# Do you want another? yes
# You have 1 coins.
# Do you want another? yes
# You have 2 coins.
# Do you want another? no
# Bye

coins = 0 


while True: 
    print(f"You have {coins} coins.")
    another_coin = input("Do you want another? ")

    if another_coin.lower() == "yes":
        coins += 1  
    elif another_coin.lower() == "no": 
        print("Bye!")
        break
    else: 
        print("Oops! Invalid response! Please choose yes or no. ")