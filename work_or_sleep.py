# Prompt the user for a day of the week just like the previous 
# problem. But this time, print "Go to work" if it's a work day
#  and "Sleep in" if it's a weekend day. Example session:

# $ python3 work_or_sleep_in.py
# Day (0-6)? 5
# Go to work
# $ python work_or_sleep_in.py
# Day (0-6)? 6
# Sleep in


# Prompt user for input

day = int(input('Day (0-6)? ')) 
day_of_week = ["Monday", "Tuesday", "Wednesday", "Thursday", "Friday", "Saturday", "Sunday"]

if 0 <= day <= 4:
    print(day_of_week[day])
    print("Go to work!")
elif 5 <= day <= 6: 
    print(day_of_week[day])
    print("Sleep in")