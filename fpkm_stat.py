#!/usr/bin/env python
import optparse
import sys
import os


def main():
    p = optparse.OptionParser()
    p.add_option('--file', '-f', default="merged.fpkm")
    options, arguments = p.parse_args()

    filename = options.file

    # open the file for reading
    filehandle = open(filename, 'r')

    firstline = filehandle.readline()
    if not firstline:
       return

    word = firstline.split()
    # 5 conditions
    rows, cols = (len(word) - 1, 5)
    arr = [[0]*cols]*rows

    while False:
       # read a single line
       line = filehandle.readline()
       if not line:
          break
       #split string in whitespaces
       word = line.split()

       for i,item in enumerate(word):
          item_val = float(item)
          if item_val > 100:
             arr[i][4] += 1
          elif item_val > 10:
             arr[i][3] += 1
          elif item_val >= 3:
             arr[i][2] += 1
          elif item_val > 0.5:
             arr[i][1] += 1
          else:
             arr[i][0] += 1

    for i in range(rows):
         for j in range(cols):
             print arr[i][j]
         print '\n'

