Genome_dir=~/Downloads/UCSF/reference
Sample_dir=~/Downloads/UCSF/fastqs
cd $Sample_dir

samtools depth -aa -m 0 Healthy_Control_001_Rep1.sorted.bam | awk 'BEGIN {{OFS="\t"}} {{c[$1] = ($3 < c[$1]) ? c[$1] : $3}} END {{for (k in c) {{print k, c[k]}}}}' | sort -k 1 >> Healthy_Control_001_Rep1.tsv
samtools depth -aa -m 0 Healthy_Control_001_Rep2.sorted.bam | awk 'BEGIN {{OFS="\t"}} {{c[$1] = ($3 < c[$1]) ? c[$1] : $3}} END {{for (k in c) {{print k, c[k]}}}}' | sort -k 1 >> Healthy_Control_001_Rep2.tsv
samtools depth -aa -m 0 Healthy_Control_002_Rep1.sorted.bam | awk 'BEGIN {{OFS="\t"}} {{c[$1] = ($3 < c[$1]) ? c[$1] : $3}} END {{for (k in c) {{print k, c[k]}}}}' | sort -k 1 >> Healthy_Control_002_Rep1.tsv
samtools depth -aa -m 0 Healthy_Control_002_Rep2.sorted.bam | awk 'BEGIN {{OFS="\t"}} {{c[$1] = ($3 < c[$1]) ? c[$1] : $3}} END {{for (k in c) {{print k, c[k]}}}}' | sort -k 1 >> Healthy_Control_002_Rep2.tsv
samtools depth -aa -m 0 Healthy_Control_003_Rep1.sorted.bam | awk 'BEGIN {{OFS="\t"}} {{c[$1] = ($3 < c[$1]) ? c[$1] : $3}} END {{for (k in c) {{print k, c[k]}}}}' | sort -k 1 >> Healthy_Control_003_Rep1.tsv
samtools depth -aa -m 0 Healthy_Control_003_Rep2.sorted.bam | awk 'BEGIN {{OFS="\t"}} {{c[$1] = ($3 < c[$1]) ? c[$1] : $3}} END {{for (k in c) {{print k, c[k]}}}}' | sort -k 1 >> Healthy_Control_003_Rep2.tsv
samtools depth -aa -m 0 Malaria_Endemic_004_Rep1.sorted.bam | awk 'BEGIN {{OFS="\t"}} {{c[$1] = ($3 < c[$1]) ? c[$1] : $3}} END {{for (k in c) {{print k, c[k]}}}}' | sort -k 1 >> Malaria_Endemic_004_Rep1.tsv
samtools depth -aa -m 0 Malaria_Endemic_004_Rep2.sorted.bam | awk 'BEGIN {{OFS="\t"}} {{c[$1] = ($3 < c[$1]) ? c[$1] : $3}} END {{for (k in c) {{print k, c[k]}}}}' | sort -k 1 >> Malaria_Endemic_004_Rep2.tsv
samtools depth -aa -m 0 Malaria_Endemic_005_Rep1.sorted.bam | awk 'BEGIN {{OFS="\t"}} {{c[$1] = ($3 < c[$1]) ? c[$1] : $3}} END {{for (k in c) {{print k, c[k]}}}}' | sort -k 1 >> Malaria_Endemic_005_Rep1.tsv
samtools depth -aa -m 0 Malaria_Endemic_005_Rep2.sorted.bam | awk 'BEGIN {{OFS="\t"}} {{c[$1] = ($3 < c[$1]) ? c[$1] : $3}} END {{for (k in c) {{print k, c[k]}}}}' | sort -k 1 >> Malaria_Endemic_005_Rep2.tsv
samtools depth -aa -m 0 Malaria_Endemic_006_Rep1.sorted.bam | awk 'BEGIN {{OFS="\t"}} {{c[$1] = ($3 < c[$1]) ? c[$1] : $3}} END {{for (k in c) {{print k, c[k]}}}}' | sort -k 1 >> Malaria_Endemic_006_Rep1.tsv
samtools depth -aa -m 0 Malaria_Endemic_006_Rep2.sorted.bam | awk 'BEGIN {{OFS="\t"}} {{c[$1] = ($3 < c[$1]) ? c[$1] : $3}} END {{for (k in c) {{print k, c[k]}}}}' | sort -k 1 >> Malaria_Endemic_006_Rep2.tsv