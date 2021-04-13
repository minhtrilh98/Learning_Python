#!/usr/bin/env python3

# Write a program that computes the running sum from 1..n
# Also, have it compute the factorial of n while you're at it
# No, you may not use math.factorial()
# Use the same loop for both calculations

n = 5
addition = 0
multiplication = 1
print('python3 sumfac.py')
for i in range (1,6):
	addition += i
	multiplication *= i
print(n,addition,multiplication)
"""
python3 sumfac.py
5 15 120
"""
