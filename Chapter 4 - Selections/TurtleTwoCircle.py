import math
import turtle


x1, y1, r1 = eval(input("Enter circle1's center x-, y-coordinates, and radius: "))
x2, y2, r2 = eval(input("Enter circle2's center x-, y-coordinates, and radius: "))

# if math.sqrt((x2 - x1) ** 2 + (y2 - y1) ** 2) <= math.fabs(r1 - r2):
#     print("Circle2 is inside Circle1.")
# elif math.sqrt((x2 - x1) ** 2 + (y2 - y1) ** 2) <= (r1 + r2):
#     print("Circle2 overlaps Circle1.")
# else:
#     print("Circle2 does not overlap Circle1.")


turtle.penup()
turtle.goto(x1, y1)
turtle.pendown()
turtle.circle(r1)
turtle.penup()

turtle.goto(x2, y2)
turtle.pendown()
turtle.circle(r2)

if math.sqrt((x2 - x1) ** 2 + (y2 - y1) ** 2) <= math.fabs(r1 - r2):
    turtle.write("Circle2 is inside Circle1.")
elif math.sqrt((x2 - x1) ** 2 + (y2 - y1) ** 2) <= (r1 + r2):
    turtle.write("Circle2 overlaps Circle1.")
else:
    turtle.write("Circle2 does not overlap Circle1.")

turtle.done()