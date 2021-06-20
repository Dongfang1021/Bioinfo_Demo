#!/usr/bin/env python
import optparse
import sys
import os

def main():
    p = optparse.OptionParser()
    p.add_option('--file', '-f', default="test.fasta")
    p.add_option('--transcriptid', '-i', default="Transcript.l500.id")
    options, arguments = p.parse_args()

    filename = options.file
    transcriptid = options.transcriptid

    # open the file for reading
    filehandle1 = open(filename, 'r')
    filehandle2 = open(transcriptid, 'r')

    line1 = filehandle1.readline()
    while True:
       # read a single line
       line2 = filehandle2.readline()
       if not line2:
          break

       flag_next_seq = False
       while True:
           if flag_next_seq:
               break
           if not line1:
               break
           word = line1.split()
           if word[0][1:] == line2.rstrip('\n'):
               print(line1.rstrip('\n'));
               while True:
                  line1 = filehandle1.readline()
                  if not line1:
                      break
                  elif line1[0] == '>':
                      flag_next_seq = True
                      break
                  else:
                      print(line1.rstrip('\n'))
           else:
              line1 = filehandle1.readline()

    # close the pointer to that file
    filehandle1.close()
    filehandle2.close()

if __name__ == '__main__':
   main()
                                                                                                                                                      1,1           All
