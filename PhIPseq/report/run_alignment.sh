Genome_dir=~/Downloads/UCSF/reference
Sample_dir=~/Downloads/UCSF/fastqs
bowtie2-build $Genome_dir/phage_library_seqs.fasta $Genome_dir/phage_library_seqs
cd $Sample_dir
cat prefix_uniq | parallel 'bowtie2 -p 2 -x ~/Downloads/UCSF/reference/phage_library_seqs -1 {}_R1.fastq.gz -2 {}_R2.fastq.gz | samtools sort -O BAM > {}.sorted.bam'