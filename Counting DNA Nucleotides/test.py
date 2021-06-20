import os, sys 
dna = sys.argv[1]
print(dna)
print("*"*100)
s=''
with open(dna, 'r') as f:
	f = f.readline()
	for i in 'ACGT':
		print(f.count(i))