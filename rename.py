#/usr/bin/env python
import pandas as pd
import argparse
import os

parser = argparse.ArgumentParser(description = " rename longname(after remove Phix) to shortname Dongfang Hu dfhu2019@gmail.com")
parser.add_argument("--input", required = True, help = " fastq file with absolute path")
parser.add_argument("--to_rename", required = True, help = "rename list file")
argv = parser.parse_args()
input = argv.input
to_rename = argv.to_rename

# os.system('cd %s' % input)
# os.system('ls *Phix_free.fastq.gz > to_rename')
# list = """
# cd %s
# ls *Phix_free.fastq.gz > to 
# """ % input
with open(os.path.join(input, to_rename), 'r') as to_rename:
	for eachline in to_rename:
		eachline = eachline.strip()
		new_name = eachline.strip().split('_')[0]
		mv_cmd = """
		cd %s
		mv %s %s_Phix_free.fastq.gz
		""" % (input, eachline, new_name)
		# print(mv_cmd)
		os.system(mv_cmd)