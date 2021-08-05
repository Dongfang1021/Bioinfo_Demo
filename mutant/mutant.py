#!/usr/bin/env python
import optparse
import re

def translate(seq):
    table = {
        'ATA': 'I', 'ATC': 'I', 'ATT': 'I', 'ATG': 'M',
        'ACA': 'T', 'ACC': 'T', 'ACG': 'T', 'ACT': 'T',
        'AAC': 'N', 'AAT': 'N', 'AAA': 'K', 'AAG': 'K',
        'AGC': 'S', 'AGT': 'S', 'AGA': 'R', 'AGG': 'R',
        'CTA': 'L', 'CTC': 'L', 'CTG': 'L', 'CTT': 'L',
        'CCA': 'P', 'CCC': 'P', 'CCG': 'P', 'CCT': 'P',
        'CAC': 'H', 'CAT': 'H', 'CAA': 'Q', 'CAG': 'Q',
        'CGA': 'R', 'CGC': 'R', 'CGG': 'R', 'CGT': 'R',
        'GTA': 'V', 'GTC': 'V', 'GTG': 'V', 'GTT': 'V',
        'GCA': 'A', 'GCC': 'A', 'GCG': 'A', 'GCT': 'A',
        'GAC': 'D', 'GAT': 'D', 'GAA': 'E', 'GAG': 'E',
        'GGA': 'G', 'GGC': 'G', 'GGG': 'G', 'GGT': 'G',
        'TCA': 'S', 'TCC': 'S', 'TCG': 'S', 'TCT': 'S',
        'TTC': 'F', 'TTT': 'F', 'TTA': 'L', 'TTG': 'L',
        'TAC': 'Y', 'TAT': 'Y', 'TAA': '_', 'TAG': '_',
        'TGC': 'C', 'TGT': 'C', 'TGA': '_', 'TGG': 'W',
    }
    protein = ""
    if len(seq) % 3 == 0:
        for i in range(0, len(seq), 3):
            codon = seq[i:i + 3]
            protein += table[codon.upper()]
    return protein

def read_seq_part(path, s, e):
    """
    read seq btw start and end in the path
    :param path: fasta file
    :param s: start position (inclusive), zero based index
    :param e: end position (inclusive), zero based index
    :return: seq btw start and end
    """

    offset = 0
    start = int(s)-1
    end = int(e)
    buffer = ""

    with open(path, 'r', newline='') as fin:
        while True:
            line = fin.readline()
            if len(line) == 0:
                break
            elif line[0].startswith('>'):
                continue
            else:
                line_length = len(line.rstrip('\n'))
                offset += line_length
                if offset < start:
                    continue

                s1 = 0
                e1 = line_length

                if offset <= start + line_length:
                    s1 = start-offset

                if offset > end:
                    e1 = end-offset

                buffer += line[s1:e1]

                if offset >= end:
                    break

    return buffer

def main():
    p = optparse.OptionParser()
    p.add_option('--input', '-i', default="cds.fasta")
    p.add_option('--position', '-p', default="239")
    p.add_option('--mutation', '-m', default="G")

    options, arguments = p.parse_args()

    filename = options.input
    position = options.position
    mutation = options.mutation
    if mutation not in 'ATGC':
        raise ValueError("Mutation must be in [ATGC]")
   

    start = ((int(position)-1)//3) * 3  # zero-based start position
    end = start + 2        # the end position of codon
    offset = int(position) - int(start) - 1
    seq = read_seq_part(filename, start, end)
    # print(seq)

    if not seq:
        print("incorrect position or position out of range: {0}".format(position))
        return

    orig_base = seq[offset]
    print("mutation position:{0}\toriginal_base:{1}\tnew_base:{2}".format(position, orig_base, mutation))

    codon_position = int(start)//3 + 1
    print("codon position: {0}".format(codon_position))

    protein = translate(seq)
    print("original codon:{0}\tamino acid:{1}".format(seq, protein))

    
    new_seq = seq[:int(offset)] + mutation + seq[int(offset)+1:]
    new_protein = translate(new_seq)
    print("mutant codon:{0}\tamino acid:{1}".format(new_seq, new_protein))


if __name__ == '__main__':
    main()
