#1 How to produce an overview of FASTQ files?
# Sequence format and type are automatically detected.
seqkit stat *.gz

#2 How do I get the GC content?
#seqkit fx2tab coverts FASTA/Q to 3-column tabular format (1st: name/ID, 2nd: sequence, 3rd: quality), and can also provide various information in new columns, including sequence length, GC content/GC skew, alphabet.
seqkit fx2tab -name -only-id-gc viral*.fna.gz | head

#3 How to I get the percentage for custom bases?
#Suppose we wish to find the percentage for A, C and A+C:
seqkit fx2tab -H -n -i -B a -B c -B ac viral.2.1.genomic.fna.gz | head -5

#4How to extract a subset of sequences with name/ID list file?
#This is a frequently used manipulation. Let’s create a sample ID list file, which may also come from some other method like a mapping result.

seqkit sample --proportion 0.001  duplicated-reads.fq.gz | seqkit seq --name --only-id > id.txt
seqkit grep --pattern-file id.txt duplicated-reads.fq.gz > duplicated-reads.subset.fq.gz

#5 How do I find FASTA/Q sequences containing degenerate bases and locate them?
#seqkit fx2tab coverts FASTA/Q to tabular format and can output the sequence alphabet in a new column. Text searching tools can then be used to filter the table.
# save the sequence IDs.
seqkit fx2tab -n -i -a viral.2.1.genomic.fna.gz | csvtk -H -t grep -f 4 -r -i -p "[^ACGT]" | csvtk -H -t cut -f 1 > id2.txt

# search and exclude.
seqkit grep --pattern-file id2.txt --invert-match viral.1.1.genomic.fna.gz > clean.fa
#Or locate the degenerate bases, e.g, N and K
seqkit grep --pattern-file id2.txt viral.2.1.genomic.fna.gz | seqkit locate --ignore-case --only-positive-strand --pattern K+ --pattern N+

#6How do I remove FASTA/Q records with duplicated sequences?
seqkit rmdup --by-seq --ignore-case duplicated-reads.fq.gz > duplicated-reads.uniq.fq.gz

#7How do I locate motif/subsequence/enzyme digest sites in FASTA/Q sequence?
seqkit locate --degenerate --ignore-case --pattern-file enzymes.fa viral.2.1.genomic.fna.gz
csvtk -t uniq -f 3 | csvtk -t pretty

#8 How do I sort a huge number of FASTA sequences by length?
seqkit sort --by-length viral.2.1.genomic.fna.gz > viral.1.1.genomic.sorted.fa
# If the files are too big, use flag --two-pass which will consume less memory.
seqkit sort --by-length --two-pass viral.2.1.genomic.fna.gz > viral.2.1.genomic.sorted.fa

#9 How do I split FASTA sequences according to information in the header?
seqkit head -n 3 viral.2.protein.faa.gz | seqkit seq --name --only-id --id-regexp "\[(.+)\]" 
seqkit split --by-id --id-regexp "\[(.+)\]" viral.1.protein.faa.gz

#10 How do I search and replace within a FASTA header using character strings from a text file?
# A regular expression, ^([^ ]+ )(\w+), was used to specify the key to be replaced, which is the first word after the sequence ID in this case. Note that we also capture the ID (^([^ ]+ )) so we can restore it in "replacement" with the capture variable ${1} (more robust than $1). And flag -I/--key-capt-idx (default: 1) is set to 2 because the key (\w+) is the second captured match. Command:
seqkit replace --kv-file changes.tsv --pattern "^([^ ]+ )(\w+) " --replacement "\${1}{kv} " --key-capt-idx 2 --keep-key viral.1.protein.faa.gz > renamed.fa

#11 How do I extract paired reads from two paired-end reads files?

seqkit rmdup duplicated-reads.fq.gz | seqkit replace --pattern " .+" --replacement " 1" | seqkit sample --proportion 0.9 --rand-seed 1 --out-file read_1.fq.gz    
seqkit rmdup duplicated-reads.fq.gz | seqkit replace --pattern " .+" --replacement " 2" | seqkit sample --proportion 0.9 --rand-seed 2 --out-file read_2.fq.gz

# number of records
seqkit stat read_1.fq.gz read_2.fq.gz 

# sequence headers
seqkit head -n 3 read_1.fq.gz | seqkit seq --name 


seqkit head -n 3 read_2.fq.gz | seqkit seq --name 

seqkit seq --name --only-id read_1.fq.gz read_2.fq.gz | sort | uniq -d > id.txt

# number of IDs
wc -l id.txt

seqkit grep --pattern-file id.txt read_1.fq.gz -o read_1.f.fq.gz
seqkit grep --pattern-file id.txt read_2.fq.gz -o read_2.f.fq.gz

seqkit seq --name --only-id read_1.f.fq.gz > read_1.f.fq.gz.id.txt
seqkit seq --name --only-id read_2.f.fq.gz > read_2.f.fq.gz.id.txt
md5sum read_*.f.fq.gz.id.txt
gzip -d -c read_1.f.fq.gz | seqkit fx2tab | sort -k1,1 -T . | seqkit tab2fx | gzip -c > read_1.f.sorted.fq.gz
gzip -d -c read_2.f.fq.gz | seqkit fx2tab | sort -k1,1 -T . | seqkit tab2fx | gzip -c > read_2.f.sorted.fq.gz

#11 How to concatenate two FASTA sequences in to one?

csvtk join -H -t <(seqkit fx2tab 1.fa) <(seqkit fx2tab 2.fa) | sed 's/\t\t//' | seqkit tab2fx




