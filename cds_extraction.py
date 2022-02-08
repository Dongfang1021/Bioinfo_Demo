#!/usr/bin/env python


from __future__ import print_function

import argparse
import gzip
import sys
from collections import defaultdict

from Bio import SeqIO
from Bio.SeqRecord import SeqRecord

parser = argparse.ArgumentParser(description="extract cds of fasta file based on gff")
parser.add_argument('--type',
                    type=str,
                    default='CDS',
                    help='gene type. "." for any types. [CDS]')
parser.add_argument('--up-stream',
                    type=int,
                    default=0,
                    help='up stream length [0]')
parser.add_argument('--down-stream',
                    type=int,
                    default=0,
                    help='down stream length [0]')
parser.add_argument('--just',
                    action="store_true",
                    help='only output up and down stream')
parser.add_argument('gff_file', type=str, help='gff file')
parser.add_argument('fasta_file', type=str, help='fasta file')
argv = vars(parser.parse_args())

if argv['type'] == None:
    	raise Exception ('You should provide gene type(such as CDS)!')
else:
	type=argv['type'].strip()


up_stream = argv['up-stream']
down_stream = argv['down-stream']
if not (up_stream >= 0 and down_stream >= 0):
    print('value of --up-stream and --down-stream should be >= 0',
          file=sys.stderr)
    sys.exit(1)

just = argv['just']
if just:
    if up_stream and down_stream or not (up_stream or down_stream):
        print(
            'when using option --just, ONE of --up-stream and --down-stream should given',
            file=sys.stderr)
        sys.exit(1)

if argv['gff_file'] == None:
    	raise Exception ('You should provide a sample list!')
else:
	gff_file=argv['gff_file'].strip()

if argv['fasta_file'] == None:
    	raise Exception ('You should provide a heatmap table file name!')
else:
	fasta_file=argv['fasta_file'].strip()


def gff_extraction(file):
    genes = defaultdict(list)
    with open(file, 'rt') as fh:
        for row in fh:
            data = row.strip().split('\t')
            if len(data) < 9:
                continue
            name = data[0]
            gene = dict()
            gene['type'], gene['start'], gene['end'], gene['strand'], gene[
                'product'
            ] = data[2], int(data[3]), int(
                data[4]), data[6], data[8]
            genes[name].append(gene)

    return genes


genes = gff_extraction(gff_file)

handle = gzip.open(fasta_file,
               'rt') if fasta_file.endswith('.gz') else open(
                   fasta_file, 'r')
for record in SeqIO.parse(handle, 'fasta'):
    name, genome = record.id, record.seq
    genomesize = len(genome)
    if name not in genes:
        continue

    for gene in genes[name]:
        if type != '.' and gene['type'].lower() != type.lower():
            continue
        seq = ''
        flag = ''
        if gene['strand'] == '+':
            if just:
                if up_stream:
                    start = gene['start'] - up_stream - 1
                    end = gene['start'] - 1
                    flag = 'jus..{}'.format(up_stream)
                else:
                    start = gene['end']
                    end = gene['end'] + down_stream
                    flag = 'jds..{}'.format(down_stream)
            else:
                start = gene['start'] - up_stream - 1
                start = 0 if start < 0 else start
                end = gene['end'] + down_stream
                if up_stream:
                    flag = 'us..{}'.format(up_stream)
                else:
                    flag = 'ds..{}'.format(down_stream)

            start = 0 if start < 0 else start
            end = genomesize - 1 if end > genomesize - 1 else e
            seq = genome[start:end]
        else:
            if just:
                if up_stream:
                    start = gene['end']
                    end = gene['end'] + up_stream
                    flag = 'jus..{}'.format(up_stream)
                else:
                    start = gene['start'] - down_stream - 1
                    end = gene['start'] - 1
                    flag = 'jds..{}'.format(down_stream)
            else:
                start = gene['start'] - down_stream - 1
                start = 0 if start < 0 else start
                end = gene['end'] + up_stream
                if up_stream:
                    flag = 'us..{}'.format(up_stream)
                else:
                    flag = 'ds..{}'.format(down_stream)

            start = 0 if start < 0 else start
            end = genomesize - 1 if end > genomesize - 1 else end
            seq = genome[start:end].reverse_complement()

        if up_stream or down_stream:
            id = '{}_{}..{}..{}_{}'.format(name, gene['start'], gene['end'],
                                           gene['strand'], flag)
        else:
            id = '{}_{}..{}..{}'.format(name, gene['start'], gene['end'],
                                        gene['strand'])
        SeqIO.write(
            SeqRecord(seq,
                      id=id,
                      description=gene['product']),
            sys.stdout,
            'fasta')
handle.close()
