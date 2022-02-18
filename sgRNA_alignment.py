#!/usr/bin/env python
# Dongfang Hu
# dfhu2019@gmail.com
import optparse
import sys
import os
from collections import Counter
import gzip 
#from iteration_utilities import first

class MyCounter(Counter):
    def __str__(self):
        return "\n".join('{} {}'.format(k, v) for k, v in self.items())

def main():
    p = optparse.OptionParser()
    p.add_option('--input', '-i', default="input.txt")
    p.add_option('--output', '-o', default="out.txt")
    p.add_option('--sgrna', '-s', default="sgrna.txt")

    options, arguments = p.parse_args()

    in_file = options.input
    out_file = options.output
    sgrna_file = options.sgrna

    # store the list of sgRNA to a collections map
    # sgrnas = set(line.strip() for line in open('sgrna_file'))
    # sgrnas = set(map(str.rstrip, open('filename.txt')))
    sgrnas = set(open(sgrna_file).read().split())
    c = MyCounter()

    # open the file for reading
    f = gzip.open(in_file, 'rt')
    i = 0
    while True:
        # read a single line
        line = f.readline()
        if not line:
            break
        i += 1
        if i % 4 != 2:
            continue
        
        # assume the length of sgRNA is 20 for all sgRNAs
        # ignore the \n in the line, so actual length strip_len is len(line) - 1
        # last slice is at line[strip_len - 20, strip_len]
        strip_len = len(line) - 1  # 90
        slicedword = set([line[i:i+20] for i in range(strip_len-19)])
        intersectword = slicedword.intersection(sgrnas)
        # can two or more sgRNA matched in the same line?
        #assert len(intersectword) <= 1
        if len(intersectword) == 1:
            c.update({list(intersectword)[0] : 1})   # next(iter(intersectword))

    # close the pointer to the input file
    f.close()

    #print(c)
    
    # c.keys()
    # write the gRNA statistics
    f = open(out_file, 'w')
    for key, value in c.items():
        # write header for each exon
        f.write("{0}:{1}".format(key, value))
        f.write("\n")
        
    # close the pointer to the output file
    f.close()

if __name__ == '__main__':
    main()
