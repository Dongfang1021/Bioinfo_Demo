#/usr/bin/env python
import pandas as pd
import argparse
import os
# read taxonomy_table.tsv and convert it to fasta format
parser = argparse.ArgumentParser(description = " control high level Dongfang Hu dfhu2019@gmail.com")
parser.add_argument("--input", required = True, help = "tsv file with absolute path")
parser.add_argument("--output", required = True, help = "output file with absolute path")
# parser.add_argument("--fastq", required = True, help = "control sample files absolute path")
argv = parser.parse_args()
input = argv.input
output = argv.output
#fastq = argv.fastq
#input = pd.read_csv(input, sep='\t', header=1, encoding="UTF-8", dtype=str)
input = open(input, 'r')
#print(input.dtypes)
fasta_file = open(os.path.join(output,'taxonomy.fasta'), "w")
i = 0
input = input.readlines()
for eachline in input[2:]:
    i += 1
    eachline = eachline.strip().split('\t')
    #print(eachline)
    fasta_file.write(">%s\n"% eachline[0])
    fasta_file.write('%s\n' % eachline[0])

taxonomy = """
java -Xmx1g -jar /Users/dongfanghu/RDP/rdp_classifier_2.13/dist/classifier.jar classify -g fungalits_unite -c 0.8 -o native_classified.txt -h hier.txt %s/taxonomy.fasta
""" % output

open(os.path.join(output, "run_taxonomy.sh"), 'w').write(taxonomy)