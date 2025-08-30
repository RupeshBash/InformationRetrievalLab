import nltk
from nltk.stem import WordNetLemmatizer
from nltk.tokenize import word_tokenize
from dataset import load_data

# Download resources if not already present
nltk.download('punkt')
nltk.download('wordnet')
nltk.download('omw-1.4')

lemmatizer = WordNetLemmatizer()

def lemmatize_text(text):
    tokens = word_tokenize(text)
    lemmatized = [lemmatizer.lemmatize(token) for token in tokens]
    return ' '.join(lemmatized)

if __name__ == "__main__":
    df = load_data()
    df["Review"] = df["Review"].apply(lemmatize_text)
    print(df)
