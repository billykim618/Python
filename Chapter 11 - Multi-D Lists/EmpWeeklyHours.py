def main():
    # Declare, create, and initialized array
    workHours = [[2, 4, 3, 4, 5, 8, 8],
                 [7, 3, 4, 3, 3, 4, 4],
                 [3, 3, 4, 3, 3, 2, 2],
                 [9, 3, 4, 7, 3, 4, 1],
                 [3, 5, 4, 3, 6, 3, 8],
                 [3, 4, 4, 6, 3, 4, 4],
                 [3, 7, 4, 8, 3, 8, 4],
                 [6, 3, 5, 9, 2, 7, 9]]

    # Create an array to store total weekly hours
    weeklyHours = []
    # your work
    for employee in workHours:
        totalHours = 0
        for hours in employee:
            totalHours += hours
        weeklyHours.append(totalHours)

    print(weeklyHours)

    count = 0
    while count < 8:
        greatestHours = 0
        greatestIndex = 0
        for employee in range(8):
            if greatestHours < weeklyHours[employee]:
                greatestHours = weeklyHours[employee]
                greatestIndex = employee
        print("Employee", greatestIndex, "worked", greatestHours)
        weeklyHours[greatestIndex] = 0
        count += 1


main()


'''
[34, 28, 20, 31, 32, 28, 37, 41]

Employee 7 worked 41
Employee 6 worked 37
Employee 0 worked 34
Employee 4 worked 32
Employee 3 worked 31
Employee 1 worked 28
Employee 5 worked 28
Employee 2 worked 20
'''
