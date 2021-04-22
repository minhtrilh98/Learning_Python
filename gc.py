#!/usr/bin/env python3

# Write a program that computes the GC% of a DNA sequence
# Format the output for 2 decimal places
# Use all three formatting methods

dna = 'ACAGAGCCAGCAGATATACAGCAGATACTAT' # feel free to change

n = 13 / len(dna)


print('%.2f' % (n)) 
print('{:.2f}'.format(n))
print(f'{13/len(dna):.2f}')

"""
python3 gc.py
0.42
0.42
0.42
"""
