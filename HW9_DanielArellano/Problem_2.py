'''
Daniel Arellano
CS 100 2020S Section 014
HW 09, March 28, 2020
'''

### Problem 2 ###

def file_stats(in_file):
    source = open(in_file)
    text = source.read()

    lines = len(text.split('\n'))
    words = len(text.split())
    characters = len(text.replace('\n', ''))
    
    print('lines = ' + str(lines))
    print('words = ' + str(words))
    print('characters = ' + str(characters))

    source.close()
