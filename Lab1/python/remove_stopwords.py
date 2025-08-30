import pandas as pd
from dataset import load_data
from nltk.corpus import stopwords
from nltk.tokenize import word_tokenize
import nltk

# Download stopwords and punkt if not already downloaded
nltk.download('stopwords')
nltk.download('punkt')

stop_words = set(stopwords.words('english'))

def remove_stopwords(text):
    """
    Remove English stopwords from the input text.
    """
    words = word_tokenize(text)  # tokenize text into words
    filtered_words = [word for word in words if word.lower() not in stop_words]
    return ' '.join(filtered_words)

if __name__ == "__main__":
    df = load_data()
    df['No Stopwords Review'] = df['Review'].apply(remove_stopwords)
    print(df[['Employee Name', 'Review', 'No Stopwords Review']])

