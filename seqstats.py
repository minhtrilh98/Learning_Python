#!/usr/bin/env python3

import argparse
import mcb185
import statistics

# Write a program that computes statistics about a fasta file
#   Number of sequences
#   Total length
#   Minimum and maximum lengths
#   Average and median lengths
#   N50 length
# Use argparse
# Make useful functions and add them to your library


parser = argparse.ArgumentParser(description='Statistic of fasta file')
# required arguments
parser.add_argument('--file', required=True, type=str,#--r1 = string
	metavar='<str>', help='required string argument')

arg = parser.parse_args()

length = []
for name, seq in mcb185.read_fasta(arg.file) :
    #print (name, len(seq))
    length.append(len(seq))
length.sort()

for i in range(0,len(length)):
    length[i] = int(length[i])

print ('List:', length)



#min & max
print('Minimum:', length[0])

print('Maximum:', length[-1])

#mean
summ = 0

for s in length:
    summ += s
Mean = summ / len(length)

print('Total length:', summ)
 
print('Mean:', Mean)

#median

print('Median:', statistics.median(length))

#N50

summ2 = 0
for value in length:
    summ2 += value
    if summ2 > summ/2:
        print('N50:', value)
        break
