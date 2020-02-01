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

dogBreeds = ['collie', 'sheepdog', 'Chow', 'Chihuaha']

# Create a list ("herdingDogs") containing the first two dog types in "dogBreeds"
herdingDogs = dogBreeds[0:2]
print(' - herdingDog = ' + str(herdingDogs))

# Create a list ("tinyDogs") containing the last two dog types in "dogBreeds"
tinyDogs = []
tinyDogs.append(dogBreeds[2])
tinyDogs.append(dogBreeds[3])
print(' - tinyDogs = ' + str(tinyDogs))

# Check if Persian is a listed dog type in "dogBreeds"
print(' - Is "Persian" in the list "dogBreeds": ' + str('Persian' in dogBreeds)) 


input('\n\nPress enter to exit...')

