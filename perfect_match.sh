#awk '$1 == "23" {print $0}' blastn_97727.txt > 23_match.txt
awk '$2 == "100.000" {print $0}' 23_match.txt > perfect_match.txt
