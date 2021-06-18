# convert classification.txt file into target format
# sequence	Kingdom	Phylum	Class	Order	Family	Genus	Species
#/usr/bin/env python
import pandas as pd
import argparse
import os
# read taxonomy_table.tsv and convert it to fasta format
parser = argparse.ArgumentParser(description = "convert classification.txt file into target format Dongfang Hu dfhu2019@gmail.com")
parser.add_argument("--input", required = True, help = "classification file with absolute path")
parser.add_argument("--output", required = True, help = "output file with absolute path")
# parser.add_argument("--fastq", required = True, help = "control sample files absolute path")
argv = parser.parse_args()
input = argv.input
output = argv.output
output = open(output,'w')
output.write('sequence\tKingdom\tPhylum\tClass\tOrder\tFamily\tGenus\tSpecies\n')
for eachline in open(input,'r'):
    eachline = eachline.strip().split('\t')
    print(eachline)
    sequence = eachline[0]
    Kingdom = eachline[5]
    #print(Kingdom)
    Phylum = eachline[8]
    Class = eachline[11]
    Order = eachline[14]
    Family = eachline[17]
    Genus = eachline[20]
    Species = eachline[23]
    output.write('%s\t%s\t%s\t%s\t%s\t%s\t%s\t%s\n' % (sequence, Kingdom, Phylum, Class, Order, Family, Genus, Species))
    