'''
Daniel Arellano
CS 100 2020S Section 014
HW 09, March 28, 2020
'''

import string

### Problem 3 ###

def repeat_words(in_file, out_file):
    source = open(in_file)
    output = open(out_file, 'w')

    for line in source.readlines():
        temp = []
        result = []
        for word in line.split():
            word = (word.strip(string.punctuation)).lower()
            if word not in temp:
                temp.append(word)
                continue
            if (word in temp) and (word not in result):
                output.write(word + ' ')
                result.append(word)
        if result != []:
            output.write('\n')

    source.close()
    output.close()
