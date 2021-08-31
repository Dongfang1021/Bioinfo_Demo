import argparse
import os
import sys
parser = argparse.ArgumentParser(description="ADH fastq rename")
parser.add_argument('--matchlist', help='matchlist genarated from ADH raw QC word, sep by tab')
parser.add_argument('--samplelist', help='ADH fastq files name list one file name per line')
argv = parser.parse_args()
matchlist = argv.matchlist
samplelist = argv.samplelist
dict = {}
cwd = os.getcwd()
release="release"
release_path = os.path.join(cwd, release)
if not os.path.isdir(release_path):
    os.mkdir(release)
output = open('run.sh', 'w')
job = open('release.sh', 'w')
for line in open(matchlist):
    line = line.strip().split('\t')
    dict[line[0]] = line[1]
for line in open(samplelist):
    line_name = line.strip()
    line = line_name.split('_')
    new_name = dict[line[0]]+"_"+str(line[1])+"_"+str(line[2])+"_"+str(line[3])+"_"+str(line[4])
    output.write("ln -sf %s/%s %s/%s\n" % (cwd, line_name, release_path, new_name))
output.write('cd %s \n' % release_path)
output.write('md5sum * > MD5.txt')
job.write('qsub -V -cwd -l vf=8G,p=4 -q gball1s.q run.sh')
