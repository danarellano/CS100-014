'''
Daniel Arellano
CS 100 2020S Section 014
HW 08, March 16, 2020
'''

### Problem 4 ###
print('Problem 4:\n')

from random import randint

def guessNumber():
    print("I'm thinking of a number in the range 0-50. You have five tries to guess it. GO!!!")
    ans = randint(0,50)
    attempts = 1
    while attempts < 6:
        guess = int(input('Guess ' + str(attempts) + '? '))
        attempts += 1
        if (guess == ans):
            return 'You are right! I was thinking of ' + str(ans) + '!'
        elif (guess > ans):
            print(str(guess) + ' is too high')
            continue
        elif (guess < ans):
            print(str(guess) + ' is too low')
            continue
            
    return 'Damn, better luck next time...'

print(guessNumber())

input('\nPress Enter to exit...')
