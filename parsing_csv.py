import pandas as pd
import glob
import re


ansi_escape = re.compile(r'\x1B(?:[@-Z\\-_]|\[[0-?]*[ -/]*[@-~])')

for project in ["antomology", "cli", "codec", "csv", "javancss", "jaxen", "jettison", "jodatime", "lang3", "dbutils", "validator", "javautil", "text", "net", "jgrapht"]:
    data = []
    
    txt_files_glob =  "LittleDarwin_results/" + project + ("/org" if project == "jaxen" else "/whitelist_*/java" if project in ["jodatime", "net", "codec", "jgrapht"] else "/java") + "/**/*.txt"
    
    for txt_file in glob.glob(txt_files_glob, recursive=True):
        java_file = txt_file.replace('.txt', '.java')
        with open(txt_file, "r") as f:
            txt_content = f.read()
            txt_content = ansi_escape.sub('', txt_content)
        
            if re.search(r"BUILD FAILURE\s*$", txt_content, re.MULTILINE):
                passed = False
            elif re.search(r"BUILD SUCCESS\s*$", txt_content, re.MULTILINE):
                passed = True
            else:
                passed = False
            with open(java_file, "r") as jf:
                java_content = jf.read()
           
            operator = re.search(r"^mutant type: (\w+)$", java_content, re.MULTILINE).groups()[0]
            line_number = re.search(r'^-.+line number in original file: (\w+)$', java_content, re.MULTILINE).groups()[0]
            mutant_node = re.search(r'^-.+mutated node: (\w+)$', java_content, re.MULTILINE).groups()[0]
            data.append({'txt_file': txt_file, 'java_file': java_file, 'passed': passed, 'operator':operator,'line_number':line_number, 'mutant_node':mutant_node})

    df = pd.DataFrame(data)
    df.to_csv("parsed_results/" + project + ".csv", index=False)