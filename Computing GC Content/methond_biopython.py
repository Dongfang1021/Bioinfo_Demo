from Bio import SeqIO
import sys
def GC(str):
	G_count = str.count('G')
	C_count = str.count('C')
	total = len(str)
	return round((G_count + C_count)*100/ total, 6)
dict= {}
for seq_record in SeqIO.parse("test.txt", "fasta"):
	gene_name = seq_record.id
	sequence = seq_record.seq
	dict[gene_name] = GC(sequence)
sorted_orders = sorted(dict.items(), key=lambda x: x[1], reverse=True)
for i in sorted_orders:
	print(i[0], i[1])