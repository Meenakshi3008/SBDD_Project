import pandas as pd
import subprocess

sirna=pd.read_csv(
"../results/ranked_siRNA.csv"
)

top=sirna.iloc[0]

parts=str(
top["Functional_score"]
).split("\n")

guide=parts[0].strip()

if len(parts)>1:
    target=parts[1].strip()
else:
    target=guide

input_seq=f"{guide}\n{target}"

result=subprocess.run(
["RNAduplex"],
input=input_seq,
text=True,
capture_output=True
)

output=result.stdout

with open(
"../results/duplex_structure.txt",
"w"
) as f:
    f.write(output)

energy=output.split()[-1]

df=pd.DataFrame({

"Target_position":[
top["Target_position"]
],

"Guide":[guide],

"Target":[target],

"Binding_energy":[energy]

})

df.to_csv(
"../results/duplex_results.csv",
index=False
)

print(output)
print("Saved")