import math


def main():
    side1, side2, side3 = eval(input("3 sides:"))
    triangle = Triangle(side1, side2, side3)
    #
    # triangle.setSide1(eval(input("Please enter side 1: ")))
    # triangle.setSide2(eval(input("Please enter side 2: ")))
    # triangle.setSide3(eval(input("Please enter side 3: ")))
    triangle.setColor(input("Please enter a color: "))
    triangle.setFilled(int(input("Please enter 1 for filled or 0 for empty: ")))

    print(triangle)
    print("Area:", triangle.getArea())
    print("Perimeter:", triangle.getPerimeter())
    print("Color:", triangle.getColor())
    print("Filled:", triangle.isFilled())


class GeometricObject:
    def __init__(self, color="green", filled=True):
        self.color = color
        self.filled = filled

    def getColor(self):
        return self.color

    def setColor(self, color):
        self.color = color

    def isFilled(self):
        return self.filled

    def setFilled(self, filled):
        self.filled = True if filled else False

    def __str__(self):
        return "Color: " + str(self.color) \
               + " and filled: " + str(self.filled)


class Triangle(GeometricObject):
    def __init__(self, side1=1.0, side2=1.0, side3=1.0):
        super().__init__()
        self.side1 = side1
        self.side2 = side2
        self.side3 = side3
        # GeometricObject.__init__(self)

    def getSide1(self):
        return self.side1

    def getSide2(self):
        return self.side2

    def getSide3(self):
        return self.side3

    def setSide1(self, side):
        self.side1 = side

    def setSide2(self, side):
        self.side2 = side

    def setSide3(self, side):
        self.side3 = side

    def getArea(self):
        s = (self.side1 + self.side2 + self.side3) / 2
        area = math.pow((s * (s - self.side1) * (s - self.side2) * (s - self.side3)), 0.5)
        return area

    def getPerimeter(self):
        return self.side1 + self.side2 + self.side3

    def __str__(self):
        return "Triangle: side 1 = " + str(self.side1) + ", side 2 = " + str(self.side2) \
                + ", side 3 = " + str(self.side3)


main()


'''
Please enter side 1: 3
Please enter side 2: 4
Please enter side 3: 5
Please enter a color: white
Please enter 1 for filled or 0 for empty: 1
Triangle: side 1 = 3, side 2 = 4, side 3 = 5
Area: 6.0
Perimeter: 12
Color: white
Filled: True
'''