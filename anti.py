#!/usr/bin/env python3

# Write a program that prints the reverse-complement of a DNA sequence
# You must use a loop and conditional

dna = 'ACTGAAAAAAAAAAA'
ss = len(dna)
i = 1

while (True): # this loop runs forever
	print(dna[ss-i],end='')
	i += 1
	if i > ss: break
print()



"""
python3 anti.py
TTTTTTTTTTTCAGT
"""
