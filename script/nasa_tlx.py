import pandas as pd

# Author: Fettah Kiran
# Email: ftth05@gmail.com

# Function to calculate NASA_sum
def calculate_nasa_sum(row):
    # Summing up the necessary columns
    return row['N_MD'] + row['N_PD'] + row['N_TD'] + row['N_P'] + row['N_E'] + row['N_F']

# Sample DataFrame (you can load your actual data here)
# data = {
#     'ID': ['T001', 'T001', 'T001', 'T001', 'T002', 'T002', 'T002', 'T002'],
#     'Day': ['Day 1', 'Day 2', 'Day 3', 'Day 4', 'Day 1', 'Day 2', 'Day 3', 'Day 4'],
#     'N_MD': [3, 4, 3, 1, 5, 3, 3, 9],
#     'N_PD': [14, 4, 16, 8, 9, 3, 3, 9],
#     'N_TD': [4, 3, 3, 2, 12, 3, 3, 9],
#     'N_P': [10, 15, 13, 14, 11, 17, 16, 8],
#     'N_E': [4, 4, 4, 4, 11, 10, 10, 14],
#     'N_F': [18, 17, 12, 11, 11, 17, 16, 8]
# }

xlsx_file = "../data/example.xlsx"
sheet_name = "NASA-TLX"
# Read the specific sheet from the Excel file
df = pd.read_excel(xlsx_file, sheet_name=sheet_name)

# Select only the first 11 columns (assuming ID is in the first column and responses in the next columns)
df = df.iloc[:, :8]

# Convert all columns except 'ID' to float
for col in df.columns:
    if col not in ["ID", "Day"]:
        df[col] = pd.to_numeric(df[col], errors='coerce')


# Apply the function to calculate NASA_sum for each row
df['NASA_sum'] = df.apply(calculate_nasa_sum, axis=1)

# Display the DataFrame with the calculated NASA_sum
print(df)

# Save results to a new file
output_file = "../results/nasa-tlx_results.xlsx"
df.to_excel(output_file, index=False)

print(f"NASA-TLX scores calculated and saved to {output_file}")
