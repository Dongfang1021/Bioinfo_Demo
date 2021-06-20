import os, sys 
dna = sys.argv[1]
print(dna)
print("*"*100)
s=''
with open(dna, 'r') as f:
	f = f.readline()
	new =f.replace('T', 'U')
	print(new)
