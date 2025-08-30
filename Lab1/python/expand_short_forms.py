import re
import pandas as pd
from dataset import load_data

# Contractions dictionary ( can expand it as needed)
contractions_dict = {
    "don't": "do not",
    "doesn't": "does not",
    "didn't": "did not",
    "can't": "cannot",
    "couldn't": "could not",
    "won't": "will not",
    "wouldn't": "would not",
    "shouldn't": "should not",
    "we're": "we are",
    "that's": "that is",
    "ain't": "am not",
    # add more as needed
}

# Create a regex pattern to identify contractions in text
contractions_re = re.compile('(%s)' % '|'.join(contractions_dict.keys()), flags=re.IGNORECASE)

def expand_contractions(text, contractions=contractions_dict):
    """
    Replace contractions in the text with their expanded form.
    """
    def replace(match):
        matched_text = match.group(0)
        lower_matched = matched_text.lower()
        expanded = contractions.get(lower_matched)
        # Preserve case: if original was uppercase, keep uppercase
        if matched_text.isupper():
            expanded = expanded.upper()
        elif matched_text[0].isupper():
            expanded = expanded.capitalize()
        return expanded
    
    return contractions_re.sub(replace, text)

if __name__ == "__main__":
    df = load_data()
    df['Expanded Review'] = df['Review'].apply(expand_contractions)
    print(df[['Employee Name', 'Review', 'Expanded Review']])
