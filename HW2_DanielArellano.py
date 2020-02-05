'''
Daniel Arellano
CS 100 2020S Section 014
HW 02, January 30, 2020
'''

### QUESTION 1 ###
print('Question 1:')

grades = ['A', 'F', 'C', 'F', 'A', 'B', 'A', 'C', 'A', 'B']
frequency = []

# Check how many time each grades appears
frequency.append(grades.count('A'))
frequency.append(grades.count('B'))
frequency.append(grades.count('C'))
frequency.append(grades.count('D'))
frequency.append(grades.count('F'))

print(' - frequency = ' + str(frequency))


### QUESTION 2 ###
print('\nQuestion 2:')

dog_breeds = ['collie', 'sheepdog', 'Chow', 'Chihuaha']

# Create a list ("herding_dogs") containing the first two dog types in "dog_breeds"
herding_dogs = dog_breeds[0:2]
print(' - herding_dog = ' + str(herding_dogs))

# Create a list ("tiny_dogs") containing the last dog type in "dog_breeds"
tiny_dogs = []
tiny_dogs.append(dog_breeds[-1])
print(' - tiny_dogs = ' + str(tiny_dogs))

# Check if Persian is a listed dog type in "dog_breeds"
print(' - Is "Persian" in the list "dog_breeds": ' + str('Persian' in dog_breeds)) 


input('\n\nPress enter to exit...')

