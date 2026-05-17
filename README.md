# Structural Bioinformatics and Drug Discovery Project

## Structure-Guided Design and Specificity-Aware Evaluation of siRNA Therapeutics Targeting IL6 in Allergic Adenoid Hypertrophy with Integration of IL4–IL13 Axis

**Author:** Meenakshi Gubba (SE24UCAB021)  
**Course:** CB2207 – Structural Bioinformatics and Drug Discovery  
**Institution:** Mahindra University  
**Semester:** 2nd Year, 2nd Semester  

---

## Project Overview

This project focuses on the computational design and evaluation of **small interfering RNA (siRNA)** candidates targeting **Interleukin-6 (IL6)**, an important cytokine involved in inflammatory signaling associated with allergic adenoid hypertrophy.

The workflow integrates biological understanding of the **IL4–IL13–IL6 inflammatory axis** with structural bioinformatics approaches to identify potentially effective IL6-targeting siRNA molecules.

The study combines sequence analysis, RNA structure prediction, thermodynamic evaluation, duplex interaction analysis, specificity screening, and biological interpretation.

---

## Objectives

The project aims to:

- Retrieve canonical IL6 transcript sequences
- Generate candidate siRNAs targeting IL6
- Predict RNA secondary structure
- Identify accessible binding regions
- Evaluate siRNA–mRNA duplex interactions
- Rank candidates using thermodynamic properties
- Assess potential off-target effects
- Interpret findings within inflammatory cytokine pathways
- Explore possible localized therapeutic delivery strategies

---

## Workflow

```text
IL6 Transcript Retrieval (NCBI)
            ↓
siRNA Candidate Generation (siDirect)
            ↓
RNA Secondary Structure Prediction (RNAfold)
            ↓
Accessible Region Identification
            ↓
siRNA–mRNA Duplex Analysis (RNAduplex)
            ↓
Thermodynamic Ranking
            ↓
BLAST Off-target Screening
            ↓
Biological Interpretation
            ↓
Candidate Prioritization
```

---

## Tools and Libraries Used

### Databases

- NCBI Entrez
- NCBI RefSeq
- NCBI BLAST

### Bioinformatics Tools

- siDirect 2.0
- ViennaRNA (RNAfold)
- ViennaRNA (RNAduplex)

### Python Libraries

- BioPython
- Pandas
- NumPy
- Matplotlib
- OS
- Shutil

---

## Project Structure

```text
SBDD_Project/

├── data/
│       IL6_mRNA.fasta
│
├── figures/
│       RNA structure plots
│       Cytokine pathway figures
│
├── results/
│       transcript_info.csv
│       siRNA_candidates.csv
│       ranked_siRNA.csv
│       final_ranked_siRNA.csv
│       duplex_results.csv
│       blast_hits.csv
│       accessible_regions.csv
│       md_stability.csv
│
├── scripts/
│       02_sidirect_design.py
│       03_rnafold_prediction.py
│       04_duplex_analysis.py
│       05_stability_analysis.py
│       06_offtarget_analysis.py
│
├── notebooks/
│       SBDD_Meenakshi.ipynb
│
├── proposal/
│       Project Proposal.docx
│
├── report/
│       Final Project Report.pdf
│
└── README.md
```

---

## Major Findings

The computational workflow identified multiple IL6-targeting siRNA candidates showing:

- Favorable thermodynamic asymmetry
- Accessible target regions
- Stable predicted duplex formation
- Strong interaction energies
- Potential therapeutic relevance

The findings suggest that selected candidates may contribute to reducing IL6-mediated inflammatory signaling. However, additional validation is required before therapeutic application.

---

## Limitations

This study is entirely computational and therefore has several limitations:

- No experimental (in vitro/in vivo) validation
- Approximate stability assessment instead of full molecular dynamics simulation
- Limited off-target prediction
- Biological effects inferred from literature rather than experimental evidence

Results should therefore be interpreted as **preliminary computational predictions**.

---

## Future Work

Future improvements may include:

- Experimental validation of top-ranked siRNA candidates
- Advanced molecular dynamics simulations
- Improved off-target prediction methods
- Investigation of nanoparticle-based delivery systems
- Expanded analysis of IL4–IL13–IL6 cytokine interactions

---

## Conclusion

This project demonstrates how computational structural bioinformatics approaches can support early-stage therapeutic design. The workflow integrates transcript analysis, RNA structure prediction, thermodynamic ranking, and biological interpretation to prioritize potential IL6-targeting siRNA therapeutics.

The study highlights both the potential and limitations of computational pipelines in RNA therapeutic development.

---

## References

Key literature includes studies on:

- RNA therapeutics
- IL6 signaling pathways
- IL4–IL13 inflammatory mechanisms
- siRNA design principles

Full citations are available in the final report.

---

## Acknowledgement

This work was completed as part of:

**CB2207 – Structural Bioinformatics and Drug Discovery**  
Mahindra University

The project combines concepts from computational biology, bioinformatics, RNA therapeutics, and structural analysis for academic research purposes.

---

## Author

**Meenakshi Gubba**  
SE24UCAB021  
Mahindra University