#!/usr/bin/env python
# Dongfang Hu
# dfhu2019@gmail.com



import argparse
from collections import Counter
"""
This script is used to sum gRNA alignment result from multi flow cell (each flow cell should contain the same libraries) into 1 file
"""
parser = argparse.ArgumentParser()
parser.add_argument('--sample_list', help='sample list')
parser.add_argument('--lib_num', help='library number in one flowcell')
parser.add_argument('--FC_num', help='Flow cell number')
parser.add_argument('--output', help='merged table')
argv = vars(parser.parse_args())


if argv['sample_list'] == None:
    	raise Exception ('You should provide a sample list!')
else:
	sample_list=argv['sample_list'].strip()


if argv['lib_num'] == None:
    	raise Exception ('You should provide library number!')
else:
	lib_num=argv['lib_num'].strip()

if argv['FC_num'] == None:
    	raise Exception ('You should provide Flow cell number!')
else:
	FC_num=argv['FC_num'].strip()

if argv['output'] == None:
    	raise Exception ('You should provide a output file name!')
else:
	output=argv['output'].strip()

############################################some functions used for data manipultation##########################################################################
def file2dict(file):
    """
    Convert tsv file into dict
    """
    file = open(file)
    file.readline()
    dict_sample = {}
    for each in file:
        each = each.strip().split("\t")
        sgRNA = each[0]
        info = each[1:]
        dict_sample[sgRNA] = info
    return dict_sample

def column_sum(lst):
    """
    Given a nested list (where sublists are of equal length), write a Python program to find the column-wise sum of the given list and return it in a new list.
    https://www.geeksforgeeks.org/python-column-wise-sum-of-nested-list/
    """  
    return [sum(i) for i in zip(*lst)]
      
#########################read sample list and convert each flowcell result into dict##############################################################################
samples = open(sample_list, 'r')
dict_sum = {}
dict_sum_counter = Counter(dict_sum)
for each in samples:
    each = each.strip()
    dict_each = file2dict(each)
    dict_count = {}
    for k, v in dict_each.items():
        dict_count[k]=tuple(v[1:(int(lib_num)+1)])
    dict_counter = Counter(dict_count)
    dict_sum_counter.update(dict_counter)
dict_out = dict(dict_sum_counter)

#######################sum gRNA count for each gRNA from different flowcell and write into new file###############################################################

template = open(sample_list, 'r')
template_a= template.readlines()[0].strip()
template_a = open(template_a, 'r')
header = template_a.readline()
output = open(output, 'w')
output.write("\t".join(header.strip().split("\t"))+"\n")
for each in template_a:
    sgRNA_id = each.strip().split("\t")[0]
    sgRNA_sequence = each.strip().split("\t")[1]
    sgRNA_count = [int(x) for x in dict_out[sgRNA_id]]
    lst = []
    for i in range(0, int(lib_num)*int(FC_num)-int(lib_num)+1, int(lib_num)):
        lst.append(sgRNA_count[i:i+int(lib_num)])
    count_sum = column_sum(lst)
    others = each.strip().split("\t")[3+int(lib_num)-1:]
    output.write(sgRNA_id+"\t"+sgRNA_sequence+"\t"+"\t".join([str(x) for x in count_sum])+"\t"+"\t".join(others)+"\n")



