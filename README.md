# Mutant-Selection-Techniques-Evaluation

This repository is a companion to the paper "_Evaluating Static Mutants Selection Techniques for Accurate Mutation Score Approximation_". It contains scripts to reproduce the results of the experiments. The data needed to reproduce the results can be found [here](https://figshare.com/s/fece5e988d03db89126d). To reproduce download the figshare zip file and extract it at the root of the project. 

## Data

### program_features.csv
  Features of the different projects used in the experiments

### full_result.csv
  Contains information on all mutant selections produced in the experiments and their performance in the format:
  
  | technique | project | percentage | min_error | mean_error | max_error | std_error | median_error |
  |-----------|---------|------------|-----------|------------|-----------|-----------|--------------|

  Where:
  - technique: the mutant selection technique used
  - project: the project the mutants were generated from
  - percentage: the sampling rate used for the technique
  - min_error: the minimum error achieved by the technique on this project at this sampling rate (across 1000 runs for techniques involving randomness)
  - mean_error: the mean error achieved by the technique on this project at this sampling rate (across 1000 runs for techniques involving randomness)
  - max_error: the maximum error achieved by the technique on this project at this sampling rate (across 1000 runs for techniques involving randomness)
  - std_error: the standard deviation of the error achieved by the technique on this project at this sampling rate (across 1000 runs for techniques involving randomness)
  - median_error: the median of the error achieved by the technique on this project at this sampling rate (across 1000 runs for techniques involving randomness)

### QRS_2025.zip
A zip file containing the data necessary to the reproduction of our results
#### LittleDarwin_results
  Folder containing the output produced by LittleDarwin on the 15 projects used in the experiments
#### selection_results
  Folder containing the mutant sets produced by the different techniques on each project

### Scripts
### parsing_csv.py
Parses LittleDarwin's output in the LittleDarwin_results folder to make it useable for the selection scripts as parsed_results/project_name.csv files
### hybrid.py
Produces subsets of mutants using the hybrid selection techniques from parsing.csv's output and saves them as selection_results/technique_name/selected_mutants_project_name.csv
### random.py
Produces subsets of mutants using the random selection sampling technique from parsing.csv's output and saves them as selection_results/technique_name/selected_mutants_project_name.csv
### stratified_sampling.py
Produces subsets of mutants using the stratified selection techniques from parsing.csv's output and saves them as selection_results/technique_name/selected_mutants_project_name.csv
### operator.py
Produces subsets of mutants using the operator group techniques (selective mutation) from parsing.csv's output and saves them as selection_results/technique_name/selected_mutants_project_name.csv
### full_results.py
Produces full_results.csv from the previous scripts' outputs and saves it in full_results.csv
### data_visualisation.ipynb
Visualises the data contained in full_results.csv
