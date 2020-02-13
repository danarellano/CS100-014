'''
Daniel Arellano
CS 100 2020S Section 014
HW 04, February 11, 2020
'''

import turtle

### QUESTION 1 ###
print('Question 1:')

a = 3
b = 4
c = 5

print('a = ' + str(a))
print('b = ' + str(b))
print('c = ' + str(c))

print('\nIs a less than b?')
if a < b:
    print('  OK')

print('\nIs c less than b?')
if c < b:
    print('  OK')

print('\nIs the sum of a and b equal to c?')
if a + b == c:
    print('  OK')

print('\nIs the sum of a^2 and b^2 equal to c^2?')
if a**2 + b**2 == c**2:
    print('  OK')


### QUESTION 2 ###
print('\nQuestion 2:')

a = 3
b = 4
c = 5

print('a = ' + str(a))
print('b = ' + str(b))
print('c = ' + str(c))

print('\nIs a less than b?')
if a < b:
    print('  OK')
else:
    print('  NOT OK')

print('\nIs c less than b?')
if c < b:
    print('  OK')
else:
    print('  NOT OK')

print('\nIs the sum of a and b equal to c?')
if a + b == c:
    print('  OK')
else:
    print('  NOT OK')

print('\nIs the sum of a^2 and b^2 equal to c^2?')
if a**2 + b**2 == c**2:
    print('  OK')
else:
    print('  NOT OK')


### Question 3 ###
print('\nQuestion 3:')

# Ask user for color, width, length, and shape to draw:
color = input('what color? ').lower()
width = int(input('what line width? '))
length = int(input('what line length? '))
shape = input('line, triangle or square? ').lower()

# Start turtle/canvas
aScreen = turtle.Screen()
shelly = turtle.Turtle()

# Set color and width
shelly.color(color)
shelly.width(width)

# Draw line (if requested)
if shape == 'line':
    shelly.forward(length)

# Draw triangle (if requested)
elif shape == 'triangle':
    # Draw one side of the triangle (three times) 
    shelly.forward(length)
    shelly.right(120)
    shelly.forward(length)
    shelly.right(120)
    shelly.forward(length)
    shelly.right(120)

# Draw square (if requested)
elif shape == 'square':
    # Draw one side of the square (four times)
    shelly.forward(length)
    shelly.right(90)
    shelly.forward(length)
    shelly.right(90)
    shelly.forward(length)
    shelly.right(90)
    shelly.forward(length)
    shelly.right(90)


input('\n\nPress enter to exit...')
