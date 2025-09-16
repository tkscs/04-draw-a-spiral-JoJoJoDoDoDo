import turtle
from scipy.constants import golden as phi

"""
The aloe polyphylla plant grows in a pattern with five golden spirals
eminating from the same center. Make a function that draws a single golden
spiral, and use that to draw a shape like the aloe polyphylla.

You may find these functions useful:

turtle.up()

turtle.down()

turtle.setposition(x, y)

turtle.setheading(degrees)

The turtle starts at position(0, 0) with heading 0 degrees.
"""

### YOUR CODE STARTS HERE
turtle.speed(15)
degrees = 5

turtle.speed(10)
for i in range(555):
    dtsf = degrees*i
    turtle.forward(2 * (phi**(dtsf / 90)))
    turtle.right(degrees)

    degrees = 5
turtle.up
turtle.setposition(0,0)

turtle.speed(10)
for i in range(555):
    dtsf = degrees*i
    turtle.forward(2 * (phi**(dtsf / 90)))
    turtle.right(degrees)


degrees = 5
turtle.setposition(1,1)

turtle.speed(10)
for i in range(555):
    dtsf = degrees*i
    turtle.forward(2 * (phi**(dtsf / 90)))
    turtle.right(degrees)









### YOUR CODE ENDS HERE

turtle.exitonclick()