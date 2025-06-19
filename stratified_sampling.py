import pandas as pd


program_features = pd.read_csv("program_features.csv")
projects = program_features["project"]

for project in projects: 
    df = pd.read_csv("parsed_results/" + project + ".csv")
    df["java_file"].replace(r'/\d+\.java$', '', regex=True, inplace=True) 
    df["operator"]
    df["line_number"] = df["java_file"]+ df["line_number"].astype(str)


    # for strat in ["line_number", "operator", "java_file"]:
    for strat in ["line_number", "operator", "java_file"]:
        results = []
        # Create strata
        df['Stratum'] = 'Strata ' + (df[strat].astype('category').cat.codes + 1).astype(str)

        grouped_df = df.groupby('Stratum', group_keys=False)

        for percentage in range(10, 100, 10):
            num_rows = int((percentage / 100) * len(df))
            false_percentages = []
            selected_mutants = []

            for i in range(1000):
            
                stratified_sample = grouped_df.sample(frac=percentage / 100)

                status_counts = stratified_sample['passed'].value_counts(normalize=True) * 100
                
                false_percentage = status_counts.get(False, 0)
                false_percentages.append(false_percentage)
                
                selected_mutants.append({
                    'Percentage': percentage,
                    'Iteration': i + 1,
                    'False_Percentage': false_percentage,
                    'Selected_Indices': stratified_sample.index.tolist()
                })
                
            results.extend(selected_mutants)

        results_df = pd.DataFrame(results)

        results_df.to_csv("selection_results/" + "SO" + "/selected_mutants_" + project + ".csv" if strat == "operator" else "selection_results/" + "SL" + "/selected_mutants_" + project + ".csv" if strat == "line_number" else "selection_results/" + "SC" + "/selected_mutants_" + project + ".csv", index=False)