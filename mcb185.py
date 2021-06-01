import random
import statistics

def read_fasta(filename):
	name = None
	seq = []
	
	with open(filename) as fp:
		while True:
			line = fp.readline()
			if line == '': break
			elif line.startswith('>'):
				if len(seq) > 0: # now is the time to return name, seq
					yield name, ''.join(seq)
				words = line.split()
				name = words[0][1:]
				seq = []
			else:
				line = line.rstrip()
				seq.append(line)
	yield name, ''.join(seq)

def CGcomposition(dna):
        c = dna.count('C')
        g = dna.count('G')
        cg = (c+g)/len(dna)
        return cg

def randseq(genome_size,cg_composition):
        seq=''
        for i in range(genome_size):
                if random.random() < cg_composition:
                        seq += random.choice('CG')
                else:
                        seq += random.choice('AT')

        return seq

def longest_orf(seq):
	max_start  = None
	max_stop   = None
	max_length = 0
	for frame in range(0, 3):
		for i in range(frame, len(seq)-2, 3):
			codon = seq[i:i+3]
			if codon == 'ATG':
				start = i
				stop = None
				for j in range(i+3, len(seq)-2, 3):
					codon = seq[j:j+3]
					if codon == 'TAA' or codon == 'TGA' or codon == 'TAG':
						stop = j
						break
				if stop != None:				
					length = stop - start + 1
					if length > max_length:
						max_length = length
						max_start  = start
						max_stop   = stop
	if max_length > 0:
		return seq[max_start:max_stop+3]
	else:
		return ''





                
