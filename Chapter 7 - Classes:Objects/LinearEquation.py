class LinearEquation:
    def __init__(self, a=0, b=0, c=0, d=0, e=0, f=0, ):
        self.a = a
        self.b = b
        self.c = c
        self.d = d
        self.e = e
        self.f = f

    def getA(self):
        return self.a

    def getB(self):
        return self.b

    def getC(self):
        return self.c

    def getD(self):
        return self.d

    def getE(self):
        return self.e

    def getF(self):
        return self.f

    def isSolvable(self):
        return self.a * self.d - self.b * self.c != 0

    def getX(self):
        return (self.e * self.d - self.b * self.f) / (self.a * self.d - self.b * self.c)

    def getY(self):
        return (self.a * self.f - self.e * self.c) / (self.a * self.d - self.b * self.c)


def main():
    a, b, c, d, e, f = eval(input("Enter a, b, c, d, e, f: "))

    eq1 = LinearEquation(a, b, c, d, e, f)
    if eq1.isSolvable():
        print("x is", eq1.getX(), "and y is", eq1.getY())
    else:
        print("The equation has no solution")


main()  # Invoke main method


'''
CONSOLE OUTPUT:

Enter a, b, c, d, e, f: 9, 4, 3, -5, -6, -21
x is -2.0 and y is 3.0

Process finished with exit code 0

Enter a, b, c, d, e, f: 1, 2, 2, 4, 4, 5
The equation has no solution

Process finished with exit code 0

'''