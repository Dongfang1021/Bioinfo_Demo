#!/usr/bin/env python
import optparse
import os, sys
import re

def readATGC_buffer(buf, s, e):
    """
    read numbers of A/T/G/C btw start and end in the path
    :param buf: fasta buffer with \n removed
    :param s: start position (inclusive), one based index
    :param e: end position (inclusive), one based index
    :return: numbers of A, T, G, C
    """

    start = int(s)-1
    end = int(e)

    buffer = buf[start:end]
    total_a = buffer.count('A') + buffer.count('a')
    total_t = buffer.count('T') + buffer.count('t')
    total_c = buffer.count('C') + buffer.count('c')
    total_g = buffer.count('G') + buffer.count('g')

    if total_a + total_t + total_g + total_c == 0:
       print("goes here {0} {1}".format(s, e))

    return (total_a, total_t, total_g, total_c)

def main():
    p = optparse.OptionParser()
    p.add_option('--fa', '-f', default="19Q3/Homo_sapiens.GRCh38.dna.chromosome.1.fa")
    p.add_option('--gtf', '-g', default="19Q3/Homo_sapiens.GRCh38.97.chr1.gtf")

    options, arguments = p.parse_args()

    fa = options.fa
    gtf = options.gtf

    with open(fa) as f:
        fa_buffer = f.read()

    # skip 1st line
    first_line_break = fa_buffer.find('\n')
    fa_buffer = fa_buffer[first_line_break+1:]

    print('{0:16}{1:12}{2:12}{3:40}{4:16}{5:8}{6:8}{7:8}{8:8}{9:5}'.format(
        "GeneID", "Start", "End", "Transcript_biotype", "GeneLength", "A", "T", "G", "C", "GC%"))

    transcript_biotype = ""
    with open(gtf) as fin:
        rows = (re.split('[ \t;"]+', line) for line in fin)
        for row in rows:
            if len(row) > 0 and row[0].startswith('#'):
                continue
            if len(row) == 0: # skip blank lines
                continue
            if row[2] == "gene": # found a gene, let's record its start and end
                gene_start, gene_end, gene_id = (row[3], row[4], row[9])
                continue
            elif row[2] == "transcript":  # found a transcript, let's record its start and end
                if bool(transcript_biotype):
                    print('{0:16}{1:12}{2:12}{3:40}{4:<16d}{5:<8d}{6:<8d}{7:<8d}{8:<8d}{9:.2f}%'.format(
                        transcript_gene_id, transcript_gene_start, transcript_gene_end,
                        transcript_biotype, int(transcript_gene_end) - int(transcript_gene_start),
                        total_a, total_t, total_g, total_c,
                        100 * (total_c + total_g) / (total_a + total_t + total_c + total_g)))

                # got a new transcript_type
                transcript_start, transcript_end, transcript_gene_id, transcript_biotype = (row[3], row[4], row[9], row[27])
                transcript_gene_start, transcript_gene_end = (gene_start, gene_end)
                if transcript_gene_id != gene_id:
                    print("Invalid gene_id in transcript {0} {1}".format(transcript_gene_id, gene_id))

                total_a, total_t, total_c, total_g = (0, 0, 0, 0)
            elif row[2] == "exon":  # found an exon, let's record its start and end
                exon_start, exon_end, exon_gene_id, exon_transcript_biotype = (row[3], row[4], row[9], row[29])

                if exon_gene_id != gene_id:
                    print("Invalid gene_id in exon {0} {1}".format(exon_gene_id, gene_id))

                if exon_transcript_biotype != transcript_biotype:
                    print("Invalid transcript_biotype in exon {0} {1}".format(exon_transcript_biotype, transcript_biotype))

                subtotal_a, subtotal_t, subtotal_g, subtotal_c = readATGC_buffer(fa_buffer, exon_start, exon_end)
                total_a += subtotal_a
                total_t += subtotal_t
                total_g += subtotal_g
                total_c += subtotal_c
            # else:
                # print(row[2]) # "CDS" "start_codon", "stop_codon" "five_prime_utr" "three_prime_utr" etc
                # sys.exit("invalid gtf file format?")

    # print last transcript_biotype
    if bool(transcript_biotype):
        print('{0:16}{1:12}{2:12}{3:40}{4:<16d}{5:<8d}{6:<8d}{7:<8d}{8:<8d}{9:.2f}%'.format(
            transcript_gene_id, transcript_gene_start, transcript_gene_end,
            transcript_biotype, int(transcript_gene_end) - int(transcript_gene_start),
            total_a, total_t, total_g, total_c,
            100 * (total_c + total_g) / (total_a + total_t + total_c + total_g)))


if __name__ == '__main__':
    main()