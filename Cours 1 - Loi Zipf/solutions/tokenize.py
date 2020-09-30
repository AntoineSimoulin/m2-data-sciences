token_pattern = re.compile(r"(?:[a-zA-ZÀ-ÖØ-ö0-9])+'?")

def tokenize(text):
    tokens = re.findall(token_pattern, text)
    tokens = [t for t in tokens]
    return tokens