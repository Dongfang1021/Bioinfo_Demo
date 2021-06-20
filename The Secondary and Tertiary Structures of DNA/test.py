import os, sys 
dna = sys.argv[1]
dna = open(dna)
dna = dna.readline()
print(dna)
dna_reverse = dna[::-1]
s = ''
for i in range(len(dna_reverse)):
	if dna_reverse[i] == 'A':
		s = s + 'T'
	if dna_reverse[i] == 'T':
		s = s + 'A'
	if dna_reverse[i] == 'G':
		s = s + 'C'
	if dna_reverse[i] == 'C':
		s = s + 'G'	
print(s)


"""
st = "AAAACCCGGT"
st = st.replace('A', 't').replace('T', 'a').replace('C', 'g').replace('G', 'c').upper()[::-1]
print st
"""