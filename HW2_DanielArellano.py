'''
Daniel Arellano
CS 100 2020S Section 014
HW 02, January 30, 2020
'''
#Question 1

grades = ['A', 'F', 'C', 'F', 'A', 'B', 'A', 'C', 'A', 'B']
frequency = []

frequency.append(grades.count('A'))
frequency.append(grades.count('B'))
frequency.append(grades.count('C'))
frequency.append(grades.count('D'))
frequency.append(grades.count('F'))

print('frequency = ' + str(frequency))


#Question 2

dogBreeds = ['collie', 'sheepdog', 'Chow', 'Chihuaha']

herdingDogs = dogBreeds[0:2]
print(herdingDogs)

tinyDogs = []
tinyDogs.append(dogBreeds[2])
tinyDogs.append(dogBreeds[3])
print(tinyDogs)

print('Persian' in dogBreeds) 

input('\n\nPress enter to exit...')

