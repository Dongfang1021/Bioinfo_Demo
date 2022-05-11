import argparse
import pandas as pd
import seaborn as sns
import matplotlib.pyplot as plt



parser = argparse.ArgumentParser()
parser.add_argument('--input',help='original file')
parser.add_argument('--output',help='new format')
argv = vars(parser.parse_args())

if argv['input'] == None:
	raise Exception ('You should provide a input file!')
else:
	input=argv['input'].strip()

if argv['output'] == None:
	raise Exception ('You should provide a output file!')
else:
    output=argv['output'].strip()



input = open(input)
header = input.readline()
sg_Name = header.strip().split("\t")[1:]
sg_Name = [x.strip().split("|")[-1] for x in sg_Name]
print(sg_Name)
#sg_Name = ["_".join(x.strip().split("_")[:-1])for x in sg_Name]
foldchange = input.readline()
foldchange = [float(x) for x in foldchange.strip().split("\t")[1:]]
print(foldchange)
plt.rcParams["figure.figsize"] = (10,10)
colors_list = ['#78C850', '#F08030',  '#6890F0',  '#A8B820',  '#483D8B', '#E0C068', '#C03028', '#F85888', '#98D8D8','#9400D3', '#1E90FF']
#sns.violinplot(x=sg_Name, y=foldchange, palette=colors_list)
ax=sns.swarmplot(x=sg_Name, y=foldchange, color="k", alpha=0.8)
ax=sns.boxplot(x=sg_Name, y=foldchange, palette=colors_list)
plt.title("foldchange different sgRNA")
plt.ylabel("foldchange")
plt.xlabel("different sgRNA")
plt.xticks(rotation=45)
plt.ylim(0, 5)
max_chars = 7
new_labels = ['\n'.join(label._text[i:i + max_chars ] 
                        for i in range(0, len(label._text), max_chars ))
              for label in ax.get_xticklabels()]

ax.set_xticklabels(new_labels)
plt.savefig(output)