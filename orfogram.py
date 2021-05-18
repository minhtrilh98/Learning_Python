#!/usr/bin/env python3

import argparse
import random
import mcb185

# In prokaryotic genomes, genes are often predicted based on length
# Long ORFs are not expected to occur by chance
# Write a program that creates a histogram of ORF lengths in random DNA
# Your library should contain new functions for the following
#    1. generating random sequence
#    2. generating ORFs from sequence
# Your program should have command line options for the following:
#    + amount of sequence to generate
#    + GC fraction of sequence
# Thought questions
#    a. how does GC fraction affect the histogram?
#    b. what is a good length threshold for a gene?


parser = argparse.ArgumentParser(description='ORF length randomization')

parser.add_argument('--size', required=False, type=int, default=4000000,
	metavar='<int>', help='Total size size. Default is [%(default)s]')
parser.add_argument('--gc', required=False, type=float, default=0.5,
	metavar='<float>', help='GC basepair fraction. [%(default)i]')
parser.add_argument('--minorf', required=False, type=int, default=96,
	metavar='<int>', help='Min size for ORF [%(default).3f]')


arg = parser.parse_args()
seq = mcb185.randseq(arg.size,arg.gc)

print(seq)

#note to self
lengths = []
for i in range(len(seq)-2):  #-2 because that last 2 nucleotide won't have 3 letter
    start = None
    stop = None
    if seq[i: i+3] == 'ATG':
        start = i
        for s in range (i, len(seq)-2,3): #i bc we want it to start @ the first ATG, -2 bc we cant make a codon out of 2 last bp, 3 is a codon
            codon = seq[s:s+3]
            #print(codon, end='')
            if codon == 'TAA' or codon == 'TGA' or codon == 'TAG':
                stop = s
                break
    if stop != None: print ('Open codon @', start,' ','Stop codon @',stop): lengths.append (stop - start + 1) 

print('Size:', arg.size,', Minimum ORF size:', arg.minorf,', CG fraction:', arg.gc)

