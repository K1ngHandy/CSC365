# CSC365

Coursework and practice exercises for **CSC 365**, focused on Python programming, data analysis, probability, statistics, and introductory data science.

## Contents

- `Week1/` — Python fundamentals, loops, strings, file I/O, lists, and basic calculations.
- `Week2/` — Introductory pandas DataFrame operations and descriptive statistics.
- `Week3/` — pandas Series, similarity measures, Jaccard similarity, and probability exercises using Titanic data.
- `Week4/` — Data visualization, distributions, standardization, correlation, sampling, confidence intervals, and hypothesis testing.
- `HW/` — Homework assignments and supporting datasets.
- `Titanic.csv` — Titanic dataset used for probability and data-analysis exercises.
- `numFile.txt`, `testingreading.txt`, `testingwriting.txt` — Text files used by file-processing exercises.

## Topics and Libraries

The exercises use Python and commonly used data-science libraries, including:

- [NumPy](https://numpy.org/) for numerical calculations
- [pandas](https://pandas.pydata.org/) for data loading and manipulation
- [Matplotlib](https://matplotlib.org/) for charts and plots
- [SciPy](https://scipy.org/) for statistical distributions and tests
- [scikit-learn](https://scikit-learn.org/) for preprocessing and scaling

## Getting Started

1. Clone the repository and change into its directory:

   ```bash
   git clone https://github.com/K1ngHandy/CSC365.git
   cd CSC365
   ```

2. Install the Python dependencies:

   ```bash
   python -m pip install numpy pandas matplotlib scipy scikit-learn
   ```

3. Run an exercise with Python. For example:

   ```bash
   python Week3/09-08.py
   python HW/hw-1.py
   ```

Some scripts display charts and require a graphical environment. Several exercises read datasets using relative paths, so run them from the repository root.

## Notes

This repository contains class notes, experiments, and homework solutions. Some files include commented-out examples from earlier lessons and may require small adjustments before being reused with different datasets or environments.

**Some code in this repository is incomplete and may require additional implementation or revision before it runs as expected.**
