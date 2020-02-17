
'''
Daniel Aellano
CS 100 2020S Section 014
HW 01, January 27, 2020
'''

### EXERCISE 1.1 ###

#Question 1
print('Hi World!')
"print 'Hi World!')" #Syntax Error
    #"Missing parenthese in call to 'print'. Did you mean print('Hi World!')?

#Question 2
greetings = 'Hi World! Again!'
"hello = Hi World! Again!'" #Syntax Error
    #Both quotation marks are required
print(greetings)

#Question 3
print(-2) #prints negative 2
print(++2) #prints postive 2
print(2++2) #prints postive 4

#Question 4
'print(09)' #Syntax Error. Invaild Token
'print(011)' #Syntax Error. Invaild Token

#Question 5
'print(2 2)' #Syntax Error


### EXERCISE 1.2 ###

#Question 1
secondsInMinute = 60
totalTimeInSeconds = 42 * secondsInMinute + 42
print(totalTimeInSeconds)

#Question 2
kilometersInMiles = 1.61
totalDistance = 10 / kilometersInMiles
print(totalDistance)

#Question 3
'Reusing totalTimeInSeconds and total distance from Exercise 1.2, Question 1'
#totalDistance = 6.211 
#totalTimeinSeconds = 2562
secondsPerMile = totalTimeInSeconds / totalDistance
#60 Seconds per Minutes
minutesPerMile = (totalTimeInSeconds / 60) / totalDistance
#3600 Seconds per Hour
milesPerHour = totalDistance / (totalTimeInSeconds / 3600) 
print(secondsPerMile)
print(minutesPerMile)
print(milesPerHour)


### Exercises 2.1 ###

#Question 1
n = 42
'42 = n' #Syntax Error. Can't assign to literal

#Question 2
#Both y and x are assign the int '1'
x = y = 1 
print (x)
print (y)

#Question 3
print('hiya'); #Run normally with semicolon

#Question 4
"print('hiya')." #Syntax Error

#Question 5
x = 2
y = 4
'print(xy)' #NameError: name 'xy' is not defined


### Exercises 2.2 ###

#Question 1
radius = 5
volume = (4/3) * 3.14 * radius**3
print(volume)

#Question 2
quantity = 60
price = 24.95
discountRate = 0.40
shippingFirstBook = 3
shippingAdditionalCopies = 0.75

finalPrice = price - (price * discountRate)
finalShipping = shippingFirstBook + (quantity - 1) * shippingAdditionalCopies

totalCost = quantity * finalPrice + finalShipping

print(totalCost)


#Question 3
startTime = 6 + 52/60
easyPace = (8 + 15/60) / 60
fastPace = (7 + 12/60) / 60
timeRunning = 2 * easyPace + 3 * fastPace
breakfastHour = startTime + timeRunning
breakfastMinute = (breakfastHour - int(breakfastHour)) * 60

print(str(int(breakfastHour)) + ':' + str(int(breakfastMinute)))

input('\nPress any key to continue')
