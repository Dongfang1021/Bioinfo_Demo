import sys
seq = sys.argv[1]
seq = open(seq)
dict = {}
def GC(str):
	G_count = str.count('G')
	C_count = str.count('C')
	total = len(str)
	return round((G_count + C_count) / total, 6)


flag_next_seq = true


while True:
	line = seq.readline()
	if not line:
		break
	if line.startswith('>'): 
		gene_name = line[1:].strip()
		total_a, total_t, total_g, total_c = 0, 0, 0, 0
		while True:
			line = seq.readline()
			if not line or line.startswith('>'):
				break
			word = line.split()
			if word[0][0] != '>':
				total_a += line.count('A')
				total_c += line.count('C')
				total_g += line.count('G')
				total_t += line.count('T')
		total_gc = total_g + total_c
		total = total_a + total_t + total_g + total_c
		gc = round(total_gc/total, 6)
		dict[gene_name] = gc
print(dict)
sorted_orders = sorted(dict.items(), key=lambda x: x[1], reverse=True)
for i in sorted_orders:
	print(i[0], i[1])


# without any package
"""
f = open('rosalind_gc.txt', 'r')

max_gc_name, max_gc_content = '', 0

buf = f.readline().rstrip()
while buf:
    seq_name, seq = buf[1:], ''
    buf = f.readline().rstrip()
    while not buf.startswith('>') and buf:
        seq = seq + buf
        buf = f.readline().rstrip()
    seq_gc_content = (seq.count('C') + seq.count('G'))/float(len(seq))
    if seq_gc_content > max_gc_content:
        max_gc_name, max_gc_content = seq_name, seq_gc_content

print('%s\n%.6f%%' % (max_gc_name, max_gc_content * 100))
f.close()
"""