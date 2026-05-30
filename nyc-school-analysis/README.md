# NYC School Analysis

Analysis of NYC public schools' SAT scores and performance metrics.

## Overview

This project analyzes data from NYC public schools, focusing on SAT scores across different boroughs and identifying top-performing schools.

## Files

- `Analysis of NYC public schools.ipynb` - Main Jupyter notebook containing the analysis
- `schools.csv` - Dataset with school performance metrics

## Analysis Highlights

The notebook performs the following analyses:

- **Math Performance**: Calculates math scores as percentages and identifies schools with math scores above 80%
- **Top Schools**: Ranks the top 10 schools by total SAT score (math + reading + writing)
- **Borough Comparison**: Groups schools by borough to compare:
  - Number of schools per borough
  - Average SAT scores by borough
  - Standard deviation of SAT scores (variability in performance)
- **Performance Variance**: Identifies which borough has the largest standard deviation in SAT scores

## Data Features

The dataset includes:
- `school_name` - Name of the school
- `borough` - NYC borough where the school is located
- `average_math` - Average math SAT score
- `average_reading` - Average reading SAT score
- `average_writing` - Average writing SAT score

## Getting Started

1. Install dependencies:
   ```bash
   pip install pandas
   ```

2. Open and run the Jupyter notebook:
   ```bash
   jupyter notebook "Analysis of NYC public schools.ipynb"
   ```

## Requirements

- Python 3.x
- pandas
