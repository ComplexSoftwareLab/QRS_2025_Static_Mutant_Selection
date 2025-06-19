import pandas as pd

program_features = pd.read_csv("program_features.csv")
projects = program_features["project"]

for project in projects:
    df = pd.read_csv("parsed_results/" + project + ".csv")

    results = []

    for percentage in range(10, 100, 10):
        num_rows = int((percentage / 100) * len(df))
        false_percentages = []
        selected_mutants = []

        for i in range(1000):
            random_rows = df.sample(n=num_rows)
            status_counts = random_rows['passed'].value_counts(normalize=True) * 100
            
            false_percentage = status_counts.get(False, 0)
            false_percentages.append(false_percentage)
            
            selected_mutants.append({
                'Percentage': percentage,
                'Iteration': i + 1,
                'False_Percentage': false_percentage,
                'Selected_Indices': random_rows.index.tolist()
            })
        
        results.extend(selected_mutants)

    results_df = pd.DataFrame(results)

    results_df.to_csv("selection_results/random/selected_mutants_" + project + ".csv", index=False)

