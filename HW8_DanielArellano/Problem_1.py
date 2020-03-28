'''
Daniel Arellano
CS 100 2020S Section 014
HW 08, March 16, 2020
'''

### Problem 1 ###
print('Problem 1:\n')

def twoWords(length, firstLetter):
    result = []
    while True: 
        word = input('Enter a ' + str(length) + '-letter word please: ')
        if len(word) == length:
            result.append(word)
            break
    while True:
        word = input('Enter a word beginning with ' + firstLetter + ' please: ')
        if (word[0]).lower() == (firstLetter).lower():
            result.append(word)
            break
    return result
            
print(twoWords(4, 'B'))

input('\nPress Enter to exit...')
