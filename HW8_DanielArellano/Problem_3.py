'''    
Daniel C. Arellano
CS 100 2019F Section 035
HW 08 - October 17, 2019 
'''

### Problem 3 ###
print('Problem 3:\n')

def newPassword():
    print('''
Please create a password:
  • At least one number
  • 8-15 Character
    ''')
    while True:
        password = input('')
        if not any(char.isdigit() for char in password):
            print('Sorry, password must have at least one number')
            continue
        if not ((len(password) >= 8) and (len(password) <= 15)):
            print('Sorry, password must be 8-15 characters')
            continue
        return 'Password created successfully!'

print(newPassword())

input('\nPress Enter to exit...')
