# SciOmics Microarray Data Workshop

Description under construction!

## Requirements

- Computer with Python
    - Tested on WSL1, WSL2, M1 Mac, M1 Mac w/ Rosetta
- Conda/Miniconda Installed ([Installer Link](https://docs.conda.io/en/latest/miniconda.html))

## Setup

Make a new conda environment:
```
conda create -n microarray python pip
```

Enter the new environment:
```
conda activate microarray
```

Install the packages:
```
pip3 install -r requirements.txt
```

Start Jupyter Lab:
```
jupyter-lab
```

## Intro
- Python Intro
- Microarray Method and Data
- PCA
- Visualization (???)
- ANOVA/F-Test
- Multiple Comparisons Correction (Benjamini-Hochberg)
- Differential Expression & Fold Change
- Pearson Correlation
- Gene Sets
- Pairwise Tukey (probably EC)
- Volcano Plots
- DepMap/CCLE