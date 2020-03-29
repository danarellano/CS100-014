'''
Daniel Arellano
CS 100 2020S Section 014
HW 09, March 28, 2020
'''

### Problem 1 ###

def file_copy(in_file, out_file):
    source = open(in_file, 'r')
    output = open(out_file, 'w')

    output.write(source.read())
    
    source.close()
    output.close()
