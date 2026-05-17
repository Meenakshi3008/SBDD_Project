import pandas as pd
from openmm.app import *
from openmm import *
from openmm.unit import *

duplex = pd.read_csv(
"../results/duplex_results.csv"
)

guide = str(
duplex.iloc[0]["Guide"]
).replace("\\n","")

target = str(
duplex.iloc[0]["Target"]
).replace("\\n","")

sequence = guide + target


# ---------- build valid pdb ----------

with open(
"../data/duplex.pdb",
"w"
) as f:

    atom=1

    for i,base in enumerate(sequence):

        x=i*3.0

        line = (
f"ATOM  {atom:5d}  P   RNA A{i+1:4d}"
f"    {x:8.3f}{0:8.3f}{0:8.3f}"
f"  1.00  0.00           P\n"
        )

        f.write(line)

        atom += 1

    f.write("END\n")

print("PDB saved")


# ---------- load into OpenMM ----------

pdb=PDBFile(
"../data/duplex.pdb"
)

forcefield=ForceField(
"amber14-all.xml"
)

system=forcefield.createSystem(
pdb.topology
)

integrator=LangevinIntegrator(

300*kelvin,

1/picosecond,

0.002*picoseconds

)

simulation=Simulation(

pdb.topology,

system,

integrator

)

simulation.context.setPositions(
pdb.positions
)

simulation.minimizeEnergy()

state=simulation.context.getState(
getEnergy=True
)

energy=state.getPotentialEnergy()

with open(
"../results/md_energy.txt",
"w"
) as f:

    f.write(
    str(energy)
    )

print(
"Energy:",
energy
)

print(
"Saved"
)