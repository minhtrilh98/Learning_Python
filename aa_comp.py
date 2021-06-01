# Make a program that reports the amino acid composition in a file of proteins
import mcb185
import math
import argparse

parser = argparse.ArgumentParser(description='All Amino Acid Composition')
# required arguments
parser.add_argument('--fasta', required=True, type=str,
	metavar='<str>', help='required string argument')
arg = parser.parse_args()

aa = {'W' , 'C' , 'H' , 'M' , 'Y' , 'Q' , 'F' , 'N' , 'P' , 'T' ,
      'R' , 'I' , 'D' , 'G' , 'A' , 'K' , 'E' , 'V' , 'L' , 'S'
}


count = {}
length = []
for name, seq in mcb185.read_fasta(arg.fasta):
    length.append(len(seq))
    for i in range (len(seq)):
        single_aa = seq[i]
        if single_aa in count: count[single_aa] += 1
        else:               count[single_aa] = 1

for i in range(0,len(length)):
    length[i] = int(length[i])

summ = 0    
for s in length:
    summ += s



for single_aa in count:
    print(single_aa, count[single_aa], (count[single_aa])/summ)

"""
    W = dna.count('W')
    C = dna.count('C')
    H = dna.count('H')
    M = dna.count('M')
    Y = dna.count('Y')
    Q = dna.count('Q')
    F = dna.count('F')
    N = dna.count('N')
    P = dna.count('P')
    T = dna.count('T')
    R = dna.count('R')
    I = dna.count('I')
    D = dna.count('D')
    G = dna.count('G')
    A = dna.count('A')
    K = dna.count('K')
    E = dna.count('E')
    V = dna.count('V')
    L = dna.count('L')
    S = dna.count('S')

 


python3 aa_comp.py -- fasta at_prots.fa | sort -nk2 
W 528 0.012054244098442994
C 801 0.018286836217524315
H 1041 0.023766038080452946
M 1097 0.025044518515136296
Y 1281 0.02924523994338158
Q 1509 0.03445048171316378
F 1842 0.04205287429797726
N 1884 0.04301173462398977
P 2051 0.046824345920277614
T 2153 0.04915300671202228
R 2320 0.05296561800831012
I 2356 0.05378749828774942
D 2573 0.05874160997214739
G 2732 0.06237158120633761
A 2772 0.06328478151682572
K 2910 0.06643532258800967
E 2989 0.06823889320122369
V 3001 0.06851285329437012
L 3950 0.09017853066070042
S 4012 0.09159399114195699
"""

