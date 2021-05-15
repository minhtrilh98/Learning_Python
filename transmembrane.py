#!/usr/bin/env python3

import sys

# Write a program that predicts if a protein is trans-membrane
# Trans-membrane proteins have the following properties
#	Signal peptide: https://en.wikipedia.org/wiki/Signal_peptide
#	Hydrophobic regions(s): https://en.wikipedia.org/wiki/Transmembrane_protein
#	No prolines in hydrophobic regions (alpha helix)
# Hydrophobicity is measued via Kyte-Dolittle
#	https://en.wikipedia.org/wiki/Hydrophilicity_plot
# For our purposes:
#	Signal peptide is 8 aa long, KD > 2.5, first 30 aa
#	Hydrophobic region is 11 aa long, KD > 2.0, after 30 aa

import mcb185
def trnsmem(seq):
        sstart = None
        sstop  = None
        max_length = 0
        for sequence in range (0,18):
                for i in range(sequence, len(seq),18):
                        trnsequence = seq[i:i+7]
                        if trnsequence[i:i+7] == 'R' or trnsequence[i:i+7] == 'N' or trnsequence[i:i+7] == 'D' or trnsequence[i:i+7] == 'E' or trnsequence[i:i+7] == 'Q' or trnsequence[i:i+7] == 'H' or trnsequence[i:i+7] == 'K' or trnsequence[i:i+7] == 'S' or trnsequence[i:i+7] == 'T' or trnsequence[i:i+7] == 'Y':
                                start = i
                                stop = None
                                for h in range (i+8, len(seq),18):
                                        trnsequence = seq[h:h+10]
                                        if trnsequence[i+8:i+18] == 'A' or trnsequence[i+8:i+18] == 'C' or trnsequence[i+8:i+18] == 'G' or trnsequence[i+8:i+18] == 'I' or trnsequence[i+8:i+18] == 'L' or trnsequence[i+8:i+18] == 'M' or trnsequence[i+8:i+18] == 'F' or trnsequence[i+8:i+18] == 'W' or trnsequence[i+8:i+18] == 'V':
                                                stop = h
                                                break
                                if stop != None:
                                        length = stop - start
                                        if length > max_length:
                                                max_length = length
                                                sstart     = start
                                                sstop      = stop
        if max_length > 0:
                return seq[sstart:sstop+17]
                seq = []
                name = None
                with open(filename) as fp:
                        while True:
                                line = fp.readline()
                                if line == '': break
                                elif line.startswith('>'):
                                        if len(seq) > 0: 
                                                yield name, ''.join(seq)
                                        words = line.split()
                                        name = words[0][1:]
                                        seq = []
                                else:   
                                        line = line.rstrip()
                                        seq.append(line)
                yield name, ''.join(seq)
        

        else:
                return ''
        

print(trnsmem(seq))


"""
python3 Programs/transmembrane.py Data/at_prots.fa
AT1G75120.1
AT1G10950.1
AT1G75110.1
AT1G74790.1
AT1G12660.1
AT1G75130.1
"""
