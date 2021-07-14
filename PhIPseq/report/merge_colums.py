import os
import sys
from collections import OrderedDict
import argparse
parser = argparse.ArgumentParser(description = "Read count metrics for all samples in one table Dongfang Hu dfhu2019@gmail.com")
parser.add_argument("--input", required = True, help = "each sample's read metrics list")
parser.add_argument("--output", required = True, help = "output file of read counts for all samples")
argv = parser.parse_args()
infiles_list = argv.input
infiles_list = open('infiles_list', 'r').readlines()
infiles_list_converted = []
for element in infiles_list:
	infiles_list_converted.append(element.strip())
outfile = argv.output
def fun(list):
	dic = OrderedDict()
	head = 'id\t'+list[0].strip().split('.')[0]
	f0 = open(list[0])
	ss = f0.readline()
	while ss.strip():
		if ss == "":
			break
		dic[ss.strip().split('\t')[0]] = ss.strip().split('\t')[1]
		ss=f0.readline()
	for each in list[1:]:
		head += '\t' + each.strip().split('.')[0]
		feach = open(each)
		everyline = feach.readline()
		while everyline.strip():
			id = everyline.strip().split('\t')[0]
			content = everyline.strip().split('\t')[1]
			dic[id] += '\t' + content
			everyline = feach.readline()
	return head, dic
fout = open(outfile, 'w')
if len(infiles_list) == 1:
	head = type + '_id\t' + infiles.split('/')[-1].split('.')[0]
	os.system("sed '1i%' %s > %s" % (head, infiles, outfile))
else:
	out = fun(infiles_list_converted)
	fout.write(out[0] + '\n')
	for k, v in out[1].items():
		fout.write(k + '\t' + v + '\n')
	fout.close()