'''
Daniel Arellano
CS 100 2020S Section 014
HW 05, February 17, 2020
'''

### QUESTION 1 ###
print('Question 1:')

months = ['January', 'February', 'March', 'April', 'May', 'June', 'July', 'August', 'September', 'October', 'November', 'December']

# Print months that start with 'J'
for month in months:
    if month[0] == 'J':
        print(month)

### Question 2 ###
print('\nQuestion 2:')

# Print numbers that are divisible by both 2 and 5
for integer in range(0,100):
    if (integer%2 == 0) and (integer%5 == 0):
        print(integer)

### Question 3 ###
print('\nQuestion 3:')

horton = "A person's a person, no matter how small."
vowels = "aeiouAEIOU"

# Print all the vowels in horton in the order they appear
for letter in horton:
    if letter in vowels:
        print(letter)


input('\n\nPress enter to exit...')
