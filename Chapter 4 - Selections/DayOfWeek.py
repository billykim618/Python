import math

year = int(input("Enter year (e.g., 2018): "))
m = int(input("Enter month (1-12): "))
if m == 1:
    m = 13
    year -= 1
if m == 2:
    m = 14
    year -= 1

q = int(input("Enter day of the month (1-31): "))
j = (year // 100)
k = year % 100

h = (q + ((26 * (m + 1)) // 10) + k + (k // 4) + (j // 4) + (5 * j)) % 7

if h == 0:
    day = "Saturday"
elif h == 1:
    day = "Sunday"
elif h == 2:
    day = "Monday"
elif h == 3:
    day = "Tuesday"
elif h == 4:
    day = "Wednesday"
elif h == 5:
    day = "Thursday"
elif h == 6:
    day = "Friday"

print("Day of the week is", day)


# CONSOLE OUTPUT:
# Enter year (e.g., 2018): 2013
# Enter month (1-12): 1
# Enter day of the month (1-31): 25
# Day of the week is Friday
#
# Process finished with exit code 0
#
# Enter year (e.g., 2018): 2018
# Enter month (1-12): 9
# Enter day of the month (1-31): 17
# Day of the week is Monday
#
# Process finished with exit code 0
