#/usr/bin/env python
import pandas as pd
import argparse
import os
# read csv line by line
parser = argparse.ArgumentParser(description = " control high level Dongfang Hu dfhu2019@gmail.com")
parser.add_argument("--input", required = True, help = "samplesheet file with absolute path")
parser.add_argument("--output", required = True, help = "control sample result directory with absolute path")
parser.add_argument("--fastq", required = True, help = "original files absolute path")
argv = parser.parse_args()
input = argv.input
output = argv.output
fastq = argv.fastq

# eachline convert to a list, which includes smaple_ID[0], Control_type[3]
control_name_neg = []
control_name_pos = []
with open(input, 'r') as samplesheet:
    for each_sample in samplesheet:
        each_sample = each_sample.strip().split(',')
        if each_sample[3] == 'NEGCON':
            control_name_neg.append(each_sample[0])
            # output.write('%s\t%s\n' % (each_sample[0], each_sample[3]))
        if each_sample[3] == 'POSCON':
            control_name_pos.append(each_sample[0])
            # output.write('%s\t%s\n' % (each_sample[0], each_sample[3]))


# soft link fastq to control directory
for each_name in control_name_neg:
    each_name = each_name.strip()
    ln_neg = """
    ln -sf %s/%s_Phix_free.fastq.gz %s/%s_neg.fastq.gz
    """ % (fastq, each_name, output, each_name)
    print(ln_neg)
    os.system(ln_neg)
for each_name in control_name_pos:
    each_name = each_name.strip()
    ln_pos = """
    ln -sf %s/%s_Phix_free.fastq.gz %s/%s_neg.fastq.gz
    """ % (fastq, each_name, output, each_name)
    os.system(ln_pos)

fastqc="""
cd %s
mkdir QC
cd QC
fastqc %s/* 
""" % (output, output)
alignment='''
cd %s
mkdir ref
ln -sf /Users/dongfanghu/Python/Phylagen/bioinformatics_demo_dataset/data/Positive_Control_References/Zymo_references.fasta %s/Zymo_references.fasta
samtools faidx ./ref/Zymo_references.fasta 
bwa index ./ref/Zymo_references.fasta 
bwa mem *fastq.gz 
''' % (output, output)
multiqc = """
cd %s
mkdir multiqc
cd multiqc
multiqc %s
""" % (output, output)
open(os.path.join(output, 'multiqc.sh'), 'w').write(multiqc)
open(os.path.join(output, 'alignment.sh'), 'w').write(alignment)
open(os.path.join(output, 'fastq.sh'), 'w').write(fastqc)
# run FASTQC and ALIGNMENT to show high level info(multiQC)
