#!/usr/bin/env python
import optparse
import sys
import os

def main():
    p = optparse.OptionParser()
    p.add_option('--file', '-f', default="test.fasta")
    p.add_option('--length', '-l', default="500")
    options, arguments = p.parse_args()

    filename = options.file
    length = options.length

    # open the file for reading
    filehandle = open(filename, 'r')
    while True:
       # read a single line
       line = filehandle.readline()
       if not line:
          break
       #split string in whitespaces
       word = line.split()
       if word[0][0] == '>':
          val = word[1].split("=")
          if int(val[1]) > int(length):
            print(word[0][1:])

    # close the pointer to that file
    filehandle.close()

if __name__ == '__main__':
   main()
                                                                                                                                                      1,1           All
