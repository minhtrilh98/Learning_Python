#!/usr/bin/env python3

# Write a program that computes typical stats
# Count, Min, Max, Mean, Std. Dev, Median
# No, you cannot import the stats library!

import sys
import math

i = 0

l = sys.argv

l2 = l[1:]

l2.sort()

number = [float(i) for i in l2]

l3 = len(l2)

mean = sum(number)/l3

stdlist = [((c - mean)**2) for c in number]
stdlist2 = math.sqrt(sum(stdlist)/l3)

Meantext = 'Mean:'
Meanmath = mean

stdtext = 'Std. dev:'
stdmath = stdlist2

Mediantext = 'Median:'
Medianmath = number[l3//2]

print('Count:', l3)
print('Minimum:',number[1])
print('Maximum:',number[l3-1])
print('{} {:.3f}'.format(Meantext, Meanmath))
print('{} {:.3f}'.format(stdtext, stdmath))
print('{} {:.3f}'.format(Mediantext, Medianmath))
"""
python3 stats.py 3 1 4 1 5
Count: 5
Minimum: 1.0
Maximum: 5.0
Mean: 2.800
Std. dev: 1.600
Median 3.000
"""
