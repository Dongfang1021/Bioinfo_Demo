#!/usr/bin/env python
import optparse
import sys
import os

def main():
    p = optparse.OptionParser()
    p.add_option('--file', '-f', default="test.fasta")
    options, arguments = p.parse_args()

    filename = options.file

    # open the file for reading
    filehandle = open(filename, 'r')

    total_a, total_t, total_c, total_g = (0, 0, 0, 0)
    while True:
       # read a single line
       line = filehandle.readline()
       if not line:
          break

       #split string in whitespaces
       word = line.split()
       if word[0][0] != '>':
          #val = word[1].split("=")
          #if int(val[1]) > int(length):
          total_a += line.count('A') + line.count('a')
          total_t += line.count('T') + line.count('t')
          total_c += line.count('C') + line.count('c')
          total_g += line.count('G') + line.count('g')

    total_gc = total_c + total_g
    total = total_a + total_t + total_c + total_g
    print('{0:8} {1}'.format('A', total_a))
    print('{0:8} {1}'.format('T', total_t))
    print('{0:8} {1}'.format('C', total_c))
    print('{0:8} {1}'.format('G', total_g))
    print('{0:8} {1}'.format('total', total))
    print('{0:8} {1:.2f}%'.format('GC', 100*total_gc/total))
    # close the pointer to that file
    filehandle.close()

if __name__ == '__main__':
   main()
                                                                                                                                                      1,1           All
