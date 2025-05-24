from nltk.stem import PorterStemmer
from nltk.tokenize import word_tokenize
from dataset import load_data

def stem_text(text):
    ps = PorterStemmer()
    words = word_tokenize(text)
    stemmed_words = [ps.stem(word) for word in words]
    return ' '.join(stemmed_words)

if __name__ == "__main__":
    import nltk
    nltk.download('punkt')  # Required for word_tokenize

    df = load_data()
    df["Review"] = df["Review"].apply(stem_text)
    print(df)
