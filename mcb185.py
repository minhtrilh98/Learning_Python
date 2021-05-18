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





                
