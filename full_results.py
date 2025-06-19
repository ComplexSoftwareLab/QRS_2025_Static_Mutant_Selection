import pandas as pd
import math

techniques = ["random", "SL", "SC", "SO", "HG_1", "HG_2", "HG_3"]

program_features = pd.read_csv("program_features.csv")
projects = program_features["project"]

full_results = None
for current_project in projects:
    
    results_project = None
    mutants_in_project =  program_features.loc[program_features["project"] == current_project]["Total_mutants"].iloc[0]
    correct_ms = program_features.loc[program_features["project"] == current_project]["Killed"].iloc[0] / mutants_in_project *100
    for technique in techniques:
        df = pd.read_csv("selection_results/" + technique + "/selected_mutants_" + current_project + ".csv", usecols=[0,1,2])
        df["error"] = abs(df["False_Percentage"] - correct_ms)/ correct_ms * 100
        df["technique"] = technique
        df["project"] = current_project

        aggregated_df = df.groupby(["technique","project","Percentage"]).agg(min_error =("error", "min"), mean_error = ("error", "mean"), max_error = ("error", "max"), std_error = ("error", "std"),  median_error = ("error", "median"))
        results_project = pd.concat([results_project, aggregated_df])    
    for technique in ["OG_1", "OG_2", "OG_3"]:
        df_2 = pd.read_csv("selection_results/Operator-based/" + current_project + "/mutants_" + technique + ".csv")
        mutants_selected = len(df_2)
        percentage = float(mutants_selected) /mutants_in_project * 100
        percentage_rounded = int(math.floor(percentage/10.0)) *10
        method_ms = len(df_2[df_2["passed"].astype(str).str.upper() == "FALSE"]) / mutants_selected * 100
        method_error = abs(method_ms - correct_ms) / correct_ms * 100 
        results_project.loc[(technique, current_project, percentage_rounded)] = [method_error, method_error, method_error, 0, method_error]
    full_results = pd.concat([full_results, results_project])

full_results.to_csv("full_results.csv")
