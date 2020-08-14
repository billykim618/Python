import turtle
import random
import math


# Draw a circle centered at (x, y) with the specified radius
def drawCircle(x=0, y=0, radius=10):
    turtle.penup()  # Pull the pen up
    turtle.goto(x, y - radius)
    turtle.pendown()  # Pull the pen down
    turtle.circle(radius)


# Draw a rectangle at (x, y) with the specified width and height
def drawRectangle(x=0, y=0, width=10, height=10):
    turtle.penup()  # Pull the pen up
    turtle.goto(x + width / 2, y + height / 2)
    turtle.pendown()  # Pull the pen down
    turtle.right(90)
    turtle.forward(height)
    turtle.right(90)
    turtle.forward(width)
    turtle.right(90)
    turtle.forward(height)
    turtle.right(90)
    turtle.forward(width)


def drawPoint(x, y):
    turtle.penup()  # Pull the pen up
    turtle.goto(x, y)
    turtle.pendown()  # Pull the pen down
    turtle.begin_fill()  # Begin to fill color in a shape
    turtle.circle(3)
    turtle.end_fill()  # Fill the shape


def main():
    # drawPoint(0, 0)
    drawCircle(50, 0, 50)   # Draw a circle with radius 50
    drawRectangle(-75, 0, 100, 100)  # Draw a rectangle/square with width and height of 100



    # Draw 10 points in the circle
    for i in range(0, 10):
        x = random.randint(0, 100)
        y = random.randint(-50, 50)
        # Distance formula from center of circle
        maxDistance = math.sqrt(math.pow(100 - 50, 2) + math.pow(0 - 0, 2))
        distance = math.sqrt(math.pow(x - 50, 2) + math.pow(y - 0, 2))
        while distance > maxDistance:
            x = random.randint(0, 100)
            y = random.randint(-50, 50)
            # Distance formula from center of circle
            maxDistance = math.sqrt(math.pow(100 - 50, 2) + math.pow(0 - 0, 2))
            distance = math.sqrt(math.pow(x - 50, 2) + math.pow(y - 0, 2))
        drawPoint(x, y)

    # Draw 10 points in the rectangle/square
    for i in range(0, 10):
        x = random.randint(-100, -25)
        y = random.randint(-50, 50)
        drawPoint(x, y)

    # Finish turtle
    turtle.done()


main()  # Invoke main method
