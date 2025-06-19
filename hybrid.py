import pandas as pd

operator_groups = { 
    "HG_1": ["NullifyObjectInitialization", "NullifyReturnValue", "RemoveMethod", "RemoveNullCheck", "NullifyInputVariable"],
    "HG_2": ["ArithmeticOperatorReplacementBinary","AssignmentOperatorReplacementShortcut","ArithmeticOperatorReplacementShortcut",
                "RelationalOperatorReplacement", "ConditionalOperatorDeletion", "ArithmeticOperatorReplacementUnary", "ConditionalOperatorReplacement",
                "LogicalOperatorReplacement", "ShiftOperatorReplacement", "RemoveMethod"],
    "HG_3": ["NullifyObjectInitialization","NullifyReturnValue","NullifyInputVariable","RemoveNullCheck","ArithmeticOperatorReplacementBinary",
          "AssignmentOperatorReplacementShortcut","ArithmeticOperatorReplacementShortcut","RelationalOperatorReplacement","ConditionalOperatorDeletion",
          "ArithmeticOperatorReplacementUnary", "ConditionalOperatorReplacement", "LogicalOperatorReplacement", "ShiftOperatorReplacement"]
}  

for project in ["antomology", "cli", "codec", "csv", "javancss", "jaxen", "jettison", "jodatime", "lang3", "text", "validator", "jgrapht", "dbutils", "net", "javautil"]:
    df = pd.read_csv("parsed_results/" + project + ".csv")

    for group, unique_operators in operator_groups.items():
        filtered_df = df[df['operator'].isin(unique_operators)]
        filtered_df['passed'] = filtered_df['passed'].astype(str).str.lower().str.strip()
        results = []

        for percentage in range(10, 100, 10):
            false_percentages = []
            selected_mutants = []

            # Number of mutants to select
            num_rows = int((percentage / 100) * len(filtered_df))

            for i in range(1000):
                
                random_rows = filtered_df.sample(n=num_rows)
                status_counts = random_rows['passed'].value_counts(normalize=True) * 100 
                false_percentage = status_counts.get('false', 0)
                false_percentages.append(false_percentage)
                selected_mutants.append({
                    'Percentage': percentage,
                    'Iteration': i + 1,
                    'False_Percentage': false_percentage,
                    'Selected_Indices': random_rows.index.tolist()
                })

            results.extend(selected_mutants)

        results_df = pd.DataFrame(results)
        results_df.to_csv("selection_results/" + group + "selected_mutants" + project + ".csv", index=False)


