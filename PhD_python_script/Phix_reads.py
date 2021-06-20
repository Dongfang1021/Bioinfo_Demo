import argparse
import json
import statistics
import os, sys
parser = argparse.ArgumentParser(description = "Phix reads Dongfang Hu dfhu2019@gmail.com")
parser.add_argument("--removelist", required = True, help = " removelist with absolute path")
parser.add_argument("--output", required = True, help = "output dir with absolute path")
argv = parser.parse_args()
output = argv.output
percentage_list = []
summary_each = open(os.path.join(output, 'summary_removed_PhiX.xls'), 'w')
summary_each.write('sample name\tpercentage reads removed\tmean of percentage of reads\n')
for each_sample in open(argv.removelist):
    each_sample = each_sample.strip()
    print(each_sample)
    filehandle = open(each_sample, "r")
    line = filehandle.readlines()[-1].rstrip()
    percentage_str = line.split('%')[0]    
    percentage_val = float(percentage_str)    
    percentage_list.append(percentage_val)
    name = each_sample.split('/')[-1].split('_')[0]
    summary_each.write('%s\t%.2f\n' % (name, percentage_val))
mean_percentage = statistics.mean(percentage_list)
print(mean_percentage)
summary_each.write('mean of percentage of reads\t-\t' + str(mean_percentage) + '\n')

