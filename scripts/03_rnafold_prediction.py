from Bio import SeqIO
import subprocess
import os

INPUT = "../data/IL6_mRNA.fasta"

OUTPUT = "../results/IL6_structure.txt"


record = SeqIO.read(
    INPUT,
    "fasta"
)

sequence = str(record.seq)


process = subprocess.run(

    ["RNAfold"],

    input=sequence,

    capture_output=True,

    text=True

)


result = process.stdout


with open(
    OUTPUT,
    "w"
) as f:

    f.write(result)


print(result)
print("\nSaved:",OUTPUT)