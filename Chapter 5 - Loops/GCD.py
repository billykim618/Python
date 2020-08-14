m,n = eval(input("Enter 2 integers (x, y): "))
print("The greatest common divisor of", m, "and", n, "is: ", end="")
while n > 0:
    m,n = n, m % n
print(m)

'''

Enter 2 integers (x, y): 24,36
The greatest common divisor of 24 and 36 is: 12

Process finished with exit code 0

Enter 2 integers (x, y): 10,10
The greatest common divisor of 10 and 10 is: 10

Process finished with exit code 0

'''