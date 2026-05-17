import subprocess

query="../results/top_siRNA.fasta"

output="../results/blast_hits.txt"

subprocess.run([

"blastn",

"-task","blastn-short",

"-query",query,

"-db","nt",

"-remote",

"-out",output,

"-outfmt","6"

])

print(
"BLAST completed"
)