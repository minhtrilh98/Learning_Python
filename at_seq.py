#!/usr/bin/env python3

import random
random.seed(1) # comment-out this line to change sequence each time

# Write a program that stores random DNA sequence in a string
# The sequence should be 30 nt long
# On average, the sequence should be 60% AT
# Calculate the actual AT fraction while generating the sequence
# Report the length, AT fraction, and sequence


length = 30
frac = 6/10

print (length, frac,end='')
for i in range(length):
    r = random.randint(1, 10)
    if   r == 1 or r == 2 or r == 3: print('A', end='')
    elif r == 4 or r == 5 or r == 6: print('T', end='')
    elif r == 7 or r == 8: print('G', end='')
    else:   print('C', end='')

print()


"""
python3 at_seq.py
30 0.6666666666666666 ATTACCGTAATCTACTATTAAGTCACAACC
"""
