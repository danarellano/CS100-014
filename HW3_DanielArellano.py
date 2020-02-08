'''
Daniel Arellano
CS 100 2020S Section 014
HW 03, February 5, 2020
'''

import turtle
import math

### QUESTION 1 ###
print('Question 1:')

aScreen = turtle.Screen()
shelly = turtle.Turtle()

# Triangle:
print('Drawing Triangle...')
# Create spacing
shelly.penup()
shelly.forward(10)
# Draw equilateral triangle (side-length = 100)
shelly.pendown()
shelly.forward(100)
shelly.left(120)
shelly.forward(100)
shelly.left(120)
shelly.forward(100)
# Go back home (reset)
shelly.penup()
shelly.left(120)
shelly.backward(10)
print('Done.')

# Square:
print('Drawing Square...')
# Create spacing
shelly.right(90)
shelly.forward(20)
shelly.left(90)
# Draw square (side-length = 100)
shelly.pendown()
shelly.forward(50)
shelly.right(90)
shelly.forward(100)
shelly.right(90)
shelly.forward(100)
shelly.right(90)
shelly.forward(100)
shelly.right(90)
shelly.forward(50)
#Go back home (reset)
shelly.penup()
shelly.left(90)
shelly.forward(20)
shelly.right(90)
print('Done.')

#Pentagon:
print('Drawing Pentagon...')
#Create spacing
shelly.left(180)
shelly.forward(20)
# Draw pentagon (side-length = 100)
shelly.pendown()
shelly.forward(100)
shelly.right(72)
shelly.forward(100)
shelly.right(72)
shelly.forward(100)
shelly.right(72)
shelly.forward(100)
shelly.right(72)
shelly.forward(100)
# Go back home (reset)
shelly.penup()
shelly.left(109)
shelly.forward(20)
print('Done.')


### QUESTION 2 ###
print('\nQuestion 2:')
shelly.clear()

shelly.forward(50)
shelly.pendown()
shelly.left(90)
shelly.circle(50)
shelly.right(90)

shelly.penup()
shelly.forward(50)
shelly.pendown()
shelly.left(90)
shelly.circle(100)
shelly.right(90)

shelly.penup()
shelly.forward(50)
shelly.pendown()
shelly.left(90)
shelly.circle(150)
shelly.right(90)

shelly.penup()
shelly.forward(50)
shelly.pendown()
shelly.left(90)
shelly.circle(200)
shelly.right(90)

shelly.penup()
shelly.setposition(0,0)


input('\n\nPress enter to exit...')

