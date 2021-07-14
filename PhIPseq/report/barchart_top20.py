import pandas as pd
import matplotlib.pyplot as plt
import argparse
import os

parser = argparse.ArgumentParser(description = "top 20 peptides Dongfang Hu dfhu2019@gmail.com")
parser.add_argument("--input", required = True, help = 'figure1 input file with absolute path')
parser.add_argument("--output", required = True, help = "output file with absolute path")
argv = parser.parse_args()
file = argv.input
file_name = file.strip().split('.')[0] + "_top20"
output = argv.output
header_list = ['id', 'counts']
counts = pd.read_csv(file, sep='\t', names = header_list)
sorted_counts_20 = counts.sort_values(by=['counts'], ascending = False).head(20)
sorted_counts_20 = sorted_counts_20.set_index('id')
plt.figure(figsize=(20, 8), dpi = 80)
sorted_counts_20.plot(kind='bar', color='SteelBlue')
plt.title( file_name +' id')
plt.xlabel('id')
plt.ylabel('count')
plt.tight_layout()
plt.savefig(os.path.join(output, file_name))

