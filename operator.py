import pandas as pd

operator_groups = { 
    "OG_1": ["NullifyObjectInitialization", "NullifyReturnValue", "RemoveMethod", "RemoveNullCheck", "NullifyInputVariable"],
    "OG_2": ["ArithmeticOperatorReplacementBinary","AssignmentOperatorReplacementShortcut","ArithmeticOperatorReplacementShortcut",
                "RelationalOperatorReplacement", "ConditionalOperatorDeletion", "ArithmeticOperatorReplacementUnary", "ConditionalOperatorReplacement",
                "LogicalOperatorReplacement", "ShiftOperatorReplacement", "RemoveMethod"],
    "OG_3": ["NullifyObjectInitialization","NullifyReturnValue","NullifyInputVariable","RemoveNullCheck","ArithmeticOperatorReplacementBinary",
          "AssignmentOperatorReplacementShortcut","ArithmeticOperatorReplacementShortcut","RelationalOperatorReplacement","ConditionalOperatorDeletion",
          "ArithmeticOperatorReplacementUnary", "ConditionalOperatorReplacement", "LogicalOperatorReplacement", "ShiftOperatorReplacement"]
}  

for project in ["antomology", "cli", "codec", "csv", "javancss", "jaxen", "jettison", "jodatime", "lang3","dbutils", "net", "validator", "javautil", "text", "jgrapht"]:
    df = pd.read_csv("parsed_results/" + project + ".csv")


    for group, unique_operators in operator_groups.items():
        filtered_df = df[df['operator'].isin(unique_operators)]
        filtered_df['passed'] = filtered_df['passed'].astype(str).str.lower().str.strip()
        results = []

        false_filtered_mutants = filtered_df[filtered_df["passed"] == "false"]

        total_filtered_mutants = len(filtered_df)
        false_filtered_count = len(false_filtered_mutants)
        false_percentage = (false_filtered_count / total_filtered_mutants) * 100

        filtered_df.to_csv("selection_results/Operator-based/" + project + "/mutants_" + group + ".csv", index=False)
