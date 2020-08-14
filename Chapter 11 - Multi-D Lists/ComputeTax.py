def main():
    status = eval(input("(0-single filer, 1-married jointly,\n" +
                        "2-married separately, 3-head of household)\n" +
                        "Enter the filing status: "))

    # Prompt the user to enter taxable income
    income = eval(input("Enter the taxable income: "))

    # Compute and display the result
    print("Tax is", format(computeTax(status, income), "7.2f"))


def computeTax(status, income):
    rates = [0.10, 0.15, 0.25, 0.28, 0.33, 0.35]

    brackets = [
        [8350, 33950, 82250, 171550, 372950],  # Single filer
        [16700, 67900, 137050, 208850, 372950],  # Married jointly
        [8350, 33950, 68525, 104425, 185475],  # Married separately
        [11950, 45500, 117450, 190200, 372950]  # Head of household
        ]

    tax = brackets[status][0] * rates[0] + \
        (brackets[status][1] - brackets[status][0]) * rates[1] + \
        (brackets[status][2] - brackets[status][1]) * rates[2] + \
        (brackets[status][3] - brackets[status][2]) * rates[3] + \
        (brackets[status][4] - brackets[status][3]) * rates[4] + \
        (income - brackets[status][4]) * rates[5]

    return tax


main()

'''
(0-single filer, 1-married jointly,
2-married separately, 3-head of household)
Enter the filing status: 0
Enter the taxable income: 400000
Tax is 117683.50
'''