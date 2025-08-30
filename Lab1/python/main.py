from dataset import load_data
from remove_emojis import remove_emojis
from lowercase import to_lowercase
# Import other modules similarly

def preprocess_pipeline(df):
    df["Review"] = df["Review"].apply(remove_emojis)
    df["Review"] = df["Review"].apply(to_lowercase)
    # Add other steps here in order
    return df

if __name__ == "__main__":
    df = load_data()
    df = preprocess_pipeline(df)
    print(df)
