def gcd(m, n):
    try:
        if m % n == 0:
            return n
        else:
            return gcd(n, m % n)
    except ZeroDivisionError:
        print("Cannot divide by zero")


def main():
    m = int(input("Enter an integer: "))
    n = int(input("Enter an integer: "))
    num = gcd(m, n)
    print("The greatest common denominator of", m, "and", n, "is:", num)


main()

'''
Enter an integer: 12
Enter an integer: 18
The greatest common denominator of 12 and 18 is: 6

Enter an integer: 2
Enter an integer: 3
The greatest common denominator of 2 and 3 is: 1
'''