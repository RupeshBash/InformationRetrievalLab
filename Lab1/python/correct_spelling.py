from textblob import TextBlob
import pandas as pd
from dataset import load_data

def correct_spelling(text):
    """
    Correct spelling errors in the input text using TextBlob.
    """
    # TextBlob returns corrected text with .correct()
    return str(TextBlob(text).correct())

if __name__ == "__main__":
    df = load_data()
    df['Corrected Review'] = df['Review'].apply(correct_spelling)
    print(df[['Employee Name', 'Review', 'Corrected Review']])
