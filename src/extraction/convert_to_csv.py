import pandas as pd
from extract_proposal import extract_proposal_to_row

def convert_file(file_path, output_csv):
    row = extract_proposal_to_row(file_path)
    df = pd.DataFrame([row])
    df.to_csv(output_csv, index=False)
    print(f"Saved structured proposal to {output_csv}")
