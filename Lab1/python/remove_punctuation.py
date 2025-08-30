import string
import pandas as pd
from dataset import load_data

def remove_punctuation(text):
    """
    Remove punctuation from the input text.
    """
    # Create a translation table that maps each punctuation character to None
    translator = str.maketrans('', '', string.punctuation)
    return text.translate(translator)

if __name__ == "__main__":
    df = load_data()
    df['No Punctuation Review'] = df['Review'].apply(remove_punctuation)
    print(df[['Employee Name', 'Review', 'No Punctuation Review']])
