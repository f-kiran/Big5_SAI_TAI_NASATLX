import pandas as pd

# Author: Fettah Kiran
# Email: ftth05@gmail.com

def calculate_big5(xlsx_file, sheet_name="Big-5"):
    """
    Calculate Big-5 personality scores based on responses in an Excel file.

    Parameters:
        xlsx_file (str): Path to the Excel file containing responses.
        sheet_name (str): Name of the sheet to read from the Excel file (default is "Big-5").
        question names: Q1 to Q10

    Outputs:
        An Excel file with calculated Big-5 scores is saved to the ../data/ directory.
    """
    # Read the specific sheet
    df = pd.read_excel(xlsx_file, sheet_name=sheet_name)

    # Select the first 11 columns
    df = df.iloc[:, :11]
    # Convert all columns except 'ID' to float
    for col in df.columns:
        if col != "ID":
            df[col] = pd.to_numeric(df[col], errors='coerce')

    # Define reverse-scored questions for each trait
    reverse_scored = {
        "Extraversion": ["Q1"],
        "Agreeableness": ["Q7"],
        "Conscientiousness": ["Q3"],
        "Neuroticism": ["Q4"],
        "Openness to Experience": ["Q5"]
    }

    # Reverse the scores
    for trait, questions in reverse_scored.items():
        for question in questions:
            if question in df.columns:
                df[question + "R"] = 6 - df[question]  # Assuming scores range from 1 to 5

    # Define calculation formula for each trait based on the given image
    formulas = {
        "Extraversion": lambda df: df["Q1R"] + df["Q5"],
        "Agreeableness": lambda df: df["Q2"] + df["Q7R"],
        "Conscientiousness": lambda df: df["Q3R"] + df["Q8"],
        "Neuroticism": lambda df: df["Q4R"] + df["Q9"],
        "Openness to Experience": lambda df: df["Q5R"] + df["Q10"]
    }

    # Calculate scores for each trait
    scores = {}
    for trait, formula in formulas.items():
        scores[trait] = formula(df)

    # Add scores to the DataFrame
    for trait, score in scores.items():
        df[trait] = score

    # Save results to a new file
    output_file = "../results/big5_results.xlsx"
    df.to_excel(output_file, index=False)
    print(f"Big-5 scores calculated and saved to {output_file}")

# Example usage
if __name__ == "__main__":
    calculate_big5("../data/example.xlsx")
