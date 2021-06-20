import argparse
import json
import statistics
import os
parser = argparse.ArgumentParser(description = "sequencing run metrics Dongfang Hu dfhu2019@gmail.com")
parser.add_argument("--file", required = True, help = "stats.json input with absolute path")
parser.add_argument("--output", required = True, help = "output dir with absolute path")
argv = parser.parse_args()
file = argv.file
output = argv.output
with open(file) as f:
    run_metrics = json.load(f)
    total_reads = run_metrics["ConversionResults"][0]["TotalClustersRaw"]
    demultiplexed_reads = run_metrics["ConversionResults"][0]["Undetermined"]['NumberReads']
    unassigned_reads = total_reads - demultiplexed_reads
    percentage_demultiplexed = (demultiplexed_reads/total_reads)*100
    sample_list = run_metrics["ConversionResults"][0]['DemuxResults']
summary_each = open(os.path.join(output, 'summary_each.xls'), 'w')
summary_each.write('sample name\tQC passed reads count\ttotal reads count\n')
total_reads_per_sample_list = []
for each_sample in sample_list:
    total_reads_per_sample = each_sample['NumberReads']
    sample_name = each_sample['SampleName']
    Q30 = float(each_sample['ReadMetrics'][0]['YieldQ30']/each_sample['ReadMetrics'][0]['Yield'])
    QC_pass = float(total_reads_per_sample*Q30)
    total_reads_per_sample_list.append(total_reads_per_sample)
    summary_each.write('%s\t%0.2f\t0.2%f\n'% (sample_name, QC_pass, total_reads_per_sample))


median_read_count = statistics.median(total_reads_per_sample_list)
mean_read_count = statistics.mean(total_reads_per_sample_list)
summary_all = open(os.path.join(output,'summary_all.xls'), 'w')
summary_all.write('totoal reads\tunassigned reads\tpercent demultiplex success\tmedian read count\tmean read count\n')
summary_all.write('%d\t%d\t%0.2f\t%.2f\t%.2f\n'%(total_reads, unassigned_reads, percentage_demultiplexed, median_read_count, mean_read_count))
