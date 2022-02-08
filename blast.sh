#blastn -db db/HSA/transcriptome -evalue 1000 -word_size 7 -num_threads 6 -task blastn-short -query seq.fa -outfmt '6 length pident qseqid qstart sseqid sstart send' > blastn_97727.txt
blastn -db db/HSA/Ensembl -evalue 1000 -word_size 7 -num_threads 6 -task blastn-short -query seq.fa -outfmt '6 length pident qseqid qstart sseqid sstart send' > blastn_97727_Ensembl.txt
