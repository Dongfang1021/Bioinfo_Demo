import re
import sys
import argparse
parser = argparse.ArgumentParser(description = "alignment summary after bowtie2 Dongfang Hu dfhu2019@gmail.com")
parser.add_argument("--input", required = True, help = 'bam flagstate files list')
parser.add_argument("--output", required = True, help = "output file of alignment summary for all samples")
argv = parser.parse_args()
alignment_totals = argv.output
input = argv.input
input = open(input, 'r')
with open("alignment_totals", "w") as op:
    print("sample\ttotal_reads\taligned_reads\tpercentage_aligned", file=op)
    for f in input:
      f = f.strip()
      sample = f.strip().split('.')[0]
      with open(f, "r") as ip:
        lines = ip.readlines()
      assert "total" in lines[0]
      assert "mapped" in lines[4]
      total_reads = int(lines[0].split()[0])
      aligned_reads = int(lines[4].split()[0])
      percentage_aligned = aligned_reads / total_reads
      print(f"{sample}\t{total_reads}\t{aligned_reads}\t{percentage_aligned:.3f}", file=op)