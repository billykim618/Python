import turtle
import math

x1, y1, x2, y2, x3, y3 = eval(input("Enter three points: "))

a = math.sqrt((x2 - x3) ** 2 + (y2 - y3) ** 2)
b = math.sqrt((((x1 - x3) * (x1 - x3)) + ((y1 - y3) * (y1 - y3))))
c = math.sqrt(pow((x1 - x2), 2) + pow((y1 - y2), 2))

A = math.degrees(math.acos((a * a - b * b - c * c) / (-2 * b * c)))
B = math.degrees(math.acos((b * b - a * a - c * c) / (-2 * a * c)))
C = math.degrees(math.acos((c * c - b * b - a * a) / (-2 * a * b)))

turtle.color("red")
turtle.goto(x1, y1)
turtle.pendown()
turtle.write(A, font=("Arial", 10, "normal"))
turtle.goto(x2,y2)
turtle.write(B, font=("Arial", 10, "normal"))
turtle.goto(x3,y3)
turtle.write(C, font=("Arial", 10, "normal"))
turtle.goto(x1,y1)

turtle.done()