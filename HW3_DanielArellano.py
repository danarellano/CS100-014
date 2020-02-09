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

print('Drawing 1st circle...')
# Create spacing (gap) between circles
shelly.forward(50)
shelly.pendown()
# Draw 1st circle (radius = 50)
shelly.left(90)
shelly.circle(50)
shelly.right(90)
print('Done.')

print('Drawing 2nd circle...')
# Create spacing (gap) between circles
shelly.penup()
shelly.forward(50)
shelly.pendown()
# Draw 2nd circle (radius = 100)
shelly.left(90)
shelly.circle(100)
shelly.right(90)
print('Done.')

print('Drawing 3rd circle...')
# Create spacing (gap) between circles
shelly.penup()
shelly.forward(50)
shelly.pendown()
# Draw 3rd circle (radius = 150)
shelly.left(90)
shelly.circle(150)
shelly.right(90)
print('Done.')

print('Drawing 4th circle...')
# Create spacing (gap) between circles
shelly.penup()
shelly.forward(50)
shelly.pendown()
# Draw 4th circle (radius = 200)
shelly.left(90)
shelly.circle(200)
shelly.right(90)
print('Done.')

print('Reseting...')
# Shelly, go back home. (reset)
shelly.penup()
shelly.setposition(0,0)
print('Done.')


### QUESTION 3 ###
print('\nQuestion 3:')

a = math.factorial(100)
print('  a)  100! = ' + str(a))
b = math.log2(1000000)
print('  b)  The log(base 2) of 1,000,000 is ' + str(b))
c = math.gcd(69,9)
print('  c)  The greatest common divisor of 63 and 49 is ' + str(c))



input('\n\nPress enter to exit...')

