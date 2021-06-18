import pandas as pd
import matplotlib.pyplot as plt
import argparse
import os
parser = argparse.ArgumentParser(description = " figure1 Dongfang Hu dfhu2019@gmail.com")
parser.add_argument("--input", required = True, help = "figure1 input file with absolute path")
parser.add_argument("--output", required = True, help = "output file with absolute path")
argv = parser.parse_args()
file = argv.input
output = argv.output
cols = ['sample name', 'QC passed reads count']
types_dict = {'sample name': str, 'QC passed reads count': float} # dtype
counts = pd.read_csv(file, sep='\t', header = 0, index_col = False, names=cols, encoding="UTF-8", dtype=types_dict) # dtype
sorted_counts = counts.sort_values(by=['QC passed reads count'], ascending=False)
sorted_counts = sorted_counts.set_index('sample name')
plt.figure(figsize=(20, 8), dpi=80)
sorted_counts.plot(kind='barh', color='SteelBlue')
plt.title('QC passed reads count per sample')
plt.xlabel('sample name')
plt.ylabel('Count')
plt.tight_layout()
plt.savefig(os.path.join(output,'figure1'))