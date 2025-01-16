import pandas as pd

# Author: Fettah Kiran
# Email: ftth05@gmail.com

def calculate_sai(mylist, question_labels):
    """
    Calculate the Subjective Assessment Index (SAI) scores based on a list of responses.

    Parameters:
        mylist (list): A list of numerical responses (e.g., 0-3).
        question_labels (list): List of question labels corresponding to the responses.

    Returns:
        tuple: A tuple with two values:
            - A list of the adjusted SAI scores (weights).
            - The total SAI score.
    """
    total = 0
    x_exception = {'Q1', 'Q2', 'Q5', 'Q8', 'Q10', 'Q11', 'Q15', 'Q16', 'Q19', 'Q20'}  # Set of question labels with exceptions
    add_list = []  # List to store adjusted scores

    for response, label in zip(mylist, question_labels):
        if label in x_exception:  # Adjusting for exception questions
            add = 4 - response + 1  # Reverse scoring
            add_list.append(add)
            total += add
        else:
            add = response
            add_list.append(add)
            total += add

    return add_list, total

def process_sai_from_excel(xlsx_file, sheet_name="SAI"):
    """
    Reads SAI data from an Excel file and calculates the SAI scores for each individual.

    Parameters:
        xlsx_file (str): Path to the Excel file containing the SAI data.
        sheet_name (str): Name of the sheet to read from the Excel file (default is "SAI").
    
    Returns:
        pd.DataFrame: DataFrame with SAI weights and total score for each ID.
    """
    # Read the specific sheet from the Excel file
    df = pd.read_excel(xlsx_file, sheet_name=sheet_name)

    # Select only the first 21 columns (assuming ID is in the first column and responses in the next columns)
    df = df.iloc[:10, :21]

    # Convert all columns except 'ID' to float
    for col in df.columns:
        if col != "ID":
            df[col] = pd.to_numeric(df[col], errors='coerce')

    # Prepare lists to store results
    sai_weights_all = []
    sai_total_all = []

    # Define question labels (assuming your columns are named Q1, Q2, ..., Q20)
    question_labels = [f"Q{i}" for i in range(1, 21)]

    # Iterate over each row (each individual)
    for _, row in df.iterrows():
        # Extract the responses (skip the 'ID' column)
        mylist = row[1:].tolist()  # Convert the row (excluding 'ID') to a list

        # Calculate SAI for the current individual
        sai_weights, sai_total = calculate_sai(mylist, question_labels)

        # Append results
        sai_weights_all.append(sai_weights)
        sai_total_all.append(sai_total)

    # Add the SAI Weights and SAI Total to the DataFrame
    df['SAI Weights'] = sai_weights_all
    df['SAI Total'] = sai_total_all

    # Save results to a new file
    output_file = "../results/sai_results.xlsx"
    df.to_excel(output_file, index=False)

    print(f"SAI scores calculated and saved to {output_file}")

    return df

# Example usage
if __name__ == "__main__":
    xlsx_file = "../data/example.xlsx"
    result_df = process_sai_from_excel(xlsx_file)

    # Display results (Optional)
    print(result_df.head())  # Print the first few rows of the final DataFrame
