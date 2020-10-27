token_pattern = re.compile(r"(?:[a-zA-ZÀ-ÖØ-ö0-9])+'?")

def tokenize(text):
    tokens = re.findall(token_pattern, text)
    tokens = [t for t in tokens]
    return tokens

X_train_df['tokens'] = X_train_df['reviews'].apply(tokenize)
X_valid_df['tokens'] = X_valid_df['reviews'].apply(tokenize)