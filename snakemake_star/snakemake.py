import os
import glob

SRA,FRR = glob_wildcards('rawReads/{sra}_{frr}.fastq')

rule all:
	input:
		expand("rawReads/{sra}_{frr}_fastqc.{extension}", sra=SRA, frr=FRR, extension=["zip", "html"])
		expand("starAligned/{sra}Aligned.sortedByCoord.out.bam", sra=SRA)

rule rawFastqc:
	input:
		rawread="rawReads/{sra}_{frr}.fastq"
	output:
		zip="rawQC/{sra}_{frr}_fastqc.zip"
		html="rawQC/{sra}_{frr}_fastqc.html"
	threads:
		1
	params:
		path="rawQC/"
	shell:
		"""
		fastqc {input.rawread} --threads {threads} -o {params.path}
		"""

rule trimmomatic:
	input:
		read1="rawReads/{sra}_1.fastq",
		read2="rawReads/{sra}_2.fastq"
	output:
		forwardPaired="trimmedReads/{sra}_1P.fastq",
		reversePaired="trimmedReads/{sra}_2P.fastq"
	threads:
		4
	params:
		basename="trimmedReads/{sra}.fastq"
		log="trimmedReads/{sra}.log"
	shell:
		"""
		trimmomatic PE -threads {threads} {input.read1} {input.read2} -baseout {params.basename} ILLUMINACLIP:TrueSeq3-PE-2.fa:2:30:10:2:keepBothReads LEADING:3 TRAILING:3 MINLEN:36 2>{params.log}
		"""

rule rawFastqc:
	input:
		read1=rules.trimmomatic.output.forwardPaired,
		read2=rules.trimmomatic.output.reversePaired
	output:
		bam="starAligned/{sra}Aligned.sortedByCoord.out.bam",
		log="starAligned/{sra}Log.final.out"
	threads:
		45
	shell:
		"""
		STAR --runThreadN {threads} --genomeDir starIndex --genomeLoad LoadAndKeep --readFilesIn {input.read1} {input.read2} --outFilterIntronMotifs RemoveNoncanonical --outFileName {params.prefix} --outSAMtype BAM SortedByCoordinate --limitBAMsortRAM 5000000000 --outReadsUnmapd Fastx
		"""