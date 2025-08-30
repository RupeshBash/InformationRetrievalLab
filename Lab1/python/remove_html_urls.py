import re
import pandas as pd
from dataset import load_data

def remove_html_and_urls(text):
    """
    Removes HTML tags and URLs from the given text.

    Parameters:
        text (str): The input text.

    Returns:
        str: Cleaned text without HTML tags and URLs.
    """
    # Remove HTML tags using regex
    text_no_html = re.sub(r'<.*?>', '', text)

    # Remove URLs
    text_no_urls = re.sub(r'http\S+|www\S+|https\S+', '', text_no_html)

    return text_no_urls.strip()

if __name__ == "__main__":
    # Load the dataset
    df = load_data()

    # Apply cleaning function to 'Review' column
    df['Cleaned Review'] = df['Review'].apply(remove_html_and_urls)

    # Display the result
    print(df[['Employee Name', 'Review', 'Cleaned Review']])
