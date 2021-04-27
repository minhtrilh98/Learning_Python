#!/usr/bin/env python3

# Write a Shannon entropy calculator: H = -sum(pi * log(pi))
# The values should come from the command line
# E.g. python3 entropy.py 0.4 0.3 0.2 0.1
# Put the probabilities into a new list
# Don't forget to convert them to numbers

import math
import sys



p = [0.1, 0.2, 0.3, 0.4]

p2 = [(c * math.log2(1/c)) for c in p]

p3 = sum(p2)

print(f'{p3:.3f}')

"""
python3 entropy.py 0.1 0.2 0.3 0.4
1.846
"""
