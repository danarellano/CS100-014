'''
Daniel Arellano
CS 100 2020S Section 014
HW 06, February 20, 2020
'''

### QUESTION 1 ###
print('Question 1:')

def hasFinalLetter(strList, letters):
    newList = []
    for word in strList:
        if word.lower()[-1] in letters.lower():
            newList.append(word)
    return newList

# Test Case 1
testList1 = ['Do', 'you', 'like', 'to', 'play', 'Jazz']
testLetters1 = 'AuiyZw'
print(hasFinalLetter(testList1, testLetters1))

# Test Case 2
testList2 = ['A', 'person\'s', 'a', 'person', 'no', 'matter', 'how', 'small']
testLetters2 = 'aeiouAEIOU'
print(hasFinalLetter(testList2, testLetters2))

# Test Case 3
testList3 = ['o','he', 'stole', 'that', 'phrase', 'from', 'HW5']
testLetters3 = 'Uwu'
print(hasFinalLetter(testList3, testLetters3))


### QUESTION 2 ###
print('\nQuestion 2:')

def isDivisible(maxInt, twoInts):
    intgerList = []
    for num in range(1, maxInt):
        if (num % twoInts[0] == 0) and (num % twoInts[1] == 0):
            intgerList.append(num)
    return intgerList

# Test Case 3
testMax1 = 50 
testInts1 = (3, 4)
print(isDivisible(testMax1, testInts1))

# Test Case 2
testMax2 = 24 
testInts2 = (2, 3)
print(isDivisible(testMax2, testInts2))

# Test Case 3
testMax3 = 15 
testInts3 = (7, 8)
print(isDivisible(testMax3, testInts3))


input('Press Enter to Exit...')
