# Structure-Guided Design of siRNA Therapeutics Targeting IL6

Computational workflow for identifying and prioritizing IL6-targeting siRNA candidates using transcript retrieval, secondary structure prediction, accessibility analysis, thermodynamic ranking, specificity assessment and visualization.

---

## Project Workflow

1. Transcript retrieval (NCBI)
2. siRNA candidate generation (siDirect)
3. Secondary structure prediction (RNAfold)
4. Duplex interaction analysis (RNAduplex)
5. Thermodynamic ranking
6. Off-target analysis (BLAST)
7. Biological interpretation
8. Visualization
9. Conceptual delivery strategies

---

## Folder Structure

data/
figures/
literature_review/
notebooks/
proposal/
report/
results/
scripts/

---

## Installation

Create environment:

pip install -r requirements.txt

---

## Required Packages

pandas  
numpy  
matplotlib  
seaborn  
biopython  
selenium  
viennarna  
openmm

---

## How to Run

Run notebook:

notebooks/SBDD_Meenakshi.ipynb

Generate figures:

notebooks/SBDD_Visualizations.ipynb

---

## Outputs

Generated files include:

- ranked_siRNA.csv
- duplex_results.csv
- final_ranked_siRNA.csv
- blast_hits.csv
- visualization PDFs

---

## Known Limitations

- Selenium automation occasionally timed out
- Full molecular dynamics simulations not completed
- Off-target predictions remain computational
- Experimental validation absent

---

## References

Reynolds et al., 2004  
Elbashir et al., 2001  
Birmingham et al., 2006

---

Author:

Meenakshi Gubba  
SE24UCAB021
