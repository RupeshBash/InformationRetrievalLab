import pandas as pd
from dataset import load_data

def to_lowercase(text):
    """
    Converts the input text to lowercase.

    Parameters:
        text (str): The text to be converted.

    Returns:
        str: Lowercased text.
    """
    return text.lower()

if __name__ == "__main__":
    # Load the dataset
    df = load_data()

    # Apply lowercase conversion to the 'Review' column
    df['Lowercased Review'] = df['Review'].apply(to_lowercase)

    # Display the original and lowercased reviews
    print(df[['Employee Name', 'Review', 'Lowercased Review']])
