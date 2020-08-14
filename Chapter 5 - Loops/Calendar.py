year = eval(input("Enter the year: "))
firstDay = eval(input("Enter the first day of the year (Sun = 0, Mon = 1, etc.): "))

# Test if leap year
if year % 400 == 0 or (year % 4 == 0 and year % 100 != 0):
    leapYear = True
else:
    leapYear = False

for i in range(1, 13):
    # Print month name
    if i == 1:
        print("\n\t\t  January", year)
    elif i == 2:
        print("\n\n\t\t February", year)
    elif i == 3:
        print("\n\n\t\t  March", year)
    elif i == 4:
        print("\n\n\t\t  April", year)
    elif i == 5:
        print("\n\n\t\t   May", year)
    elif i == 6:
        print("\n\n\t\t   June", year)
    elif i == 7:
        print("\n\n\t\t   July", year)
    elif i == 8:
        print("\n\n\t\t  August", year)
    elif i == 9:
        print("\n\n\t\t September", year)
    elif i == 10:
        print("\n\n\t\t  October", year)
    elif i == 11:
        print("\n\n\t\t November", year)
    elif i == 12:
        print("\n\n\t\t December", year)

    print("SUN  MON  TUE  WED  THU  FRI  SAT")
    print("---------------------------------")

    # Add necessary spaces before first day in each month
    for j in range(0, firstDay):
        print("     ", end="")

    # Months with 31 days
    if i == 1 or i == 3 or i == 5 or i == 7 or \
    i == 8 or i == 10 or i == 12:
        for day in range(1, 32):
            print("{0:<5d}".format(day), end="")
            if (day + firstDay) % 7 == 0:
                print("")

    # Months with 30 days
    elif i == 4 or i == 6 or i == 9 or i == 11:
        for day in range(1, 31):
            print("{0:<5d}".format(day), end="")
            if (day + firstDay) % 7 == 0:
                print("")

    # February and leap year
    elif i == 2 and leapYear:
        for day in range(1, 30):
            print("{0:<5d}".format(day), end="")
            if (day + firstDay) % 7 == 0:
                print("")

    # February and not leap year
    elif i == 2 and not leapYear:
        for day in range(1, 29):
            print("{0:<5d}".format(day), end="")
            if (day + firstDay) % 7 == 0:
                print("")

    if i == 1 or i == 3 or i == 5 or i == 7 or \
    i == 8 or i == 10 or i == 12:
        firstDay += 3
    elif i == 4 or i == 6 or i == 9 or i == 11:
            firstDay += 2
    elif i == 2 and leapYear:
        firstDay += 1
    while firstDay > 6:
        firstDay -= 7

'''
Enter the year: 2016
Enter the first day of the year: 5

		  January 2016
SUN  MON  TUE  WED  THU  FRI  SAT
---------------------------------
                         1    2    
3    4    5    6    7    8    9    
10   11   12   13   14   15   16   
17   18   19   20   21   22   23   
24   25   26   27   28   29   30   
31   

		 February 2016
SUN  MON  TUE  WED  THU  FRI  SAT
---------------------------------
     1    2    3    4    5    6    
7    8    9    10   11   12   13   
14   15   16   17   18   19   20   
21   22   23   24   25   26   27   
28   29   

		  March 2016
SUN  MON  TUE  WED  THU  FRI  SAT
---------------------------------
          1    2    3    4    5    
6    7    8    9    10   11   12   
13   14   15   16   17   18   19   
20   21   22   23   24   25   26   
27   28   29   30   31   

		  April 2016
SUN  MON  TUE  WED  THU  FRI  SAT
---------------------------------
                         1    2    
3    4    5    6    7    8    9    
10   11   12   13   14   15   16   
17   18   19   20   21   22   23   
24   25   26   27   28   29   30   


		   May 2016
SUN  MON  TUE  WED  THU  FRI  SAT
---------------------------------
1    2    3    4    5    6    7    
8    9    10   11   12   13   14   
15   16   17   18   19   20   21   
22   23   24   25   26   27   28   
29   30   31   

		   June 2016
SUN  MON  TUE  WED  THU  FRI  SAT
---------------------------------
               1    2    3    4    
5    6    7    8    9    10   11   
12   13   14   15   16   17   18   
19   20   21   22   23   24   25   
26   27   28   29   30   

		   July 2016
SUN  MON  TUE  WED  THU  FRI  SAT
---------------------------------
                         1    2    
3    4    5    6    7    8    9    
10   11   12   13   14   15   16   
17   18   19   20   21   22   23   
24   25   26   27   28   29   30   
31   

		  August 2016
SUN  MON  TUE  WED  THU  FRI  SAT
---------------------------------
     1    2    3    4    5    6    
7    8    9    10   11   12   13   
14   15   16   17   18   19   20   
21   22   23   24   25   26   27   
28   29   30   31   

		 September 2016
SUN  MON  TUE  WED  THU  FRI  SAT
---------------------------------
                    1    2    3    
4    5    6    7    8    9    10   
11   12   13   14   15   16   17   
18   19   20   21   22   23   24   
25   26   27   28   29   30   

		  October 2016
SUN  MON  TUE  WED  THU  FRI  SAT
---------------------------------
                              1    
2    3    4    5    6    7    8    
9    10   11   12   13   14   15   
16   17   18   19   20   21   22   
23   24   25   26   27   28   29   
30   31   

		 November 2016
SUN  MON  TUE  WED  THU  FRI  SAT
---------------------------------
          1    2    3    4    5    
6    7    8    9    10   11   12   
13   14   15   16   17   18   19   
20   21   22   23   24   25   26   
27   28   29   30   

		 December 2016
SUN  MON  TUE  WED  THU  FRI  SAT
---------------------------------
                    1    2    3    
4    5    6    7    8    9    10   
11   12   13   14   15   16   17   
18   19   20   21   22   23   24   
25   26   27   28   29   30   31   

Process finished with exit code 0
'''