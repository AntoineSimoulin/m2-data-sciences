stemmer = FrenchStemmer()

def clean_corpus(corpus):
    for i in range(len(corpus)):
        corpus[i] = unidecode.unidecode(corpus[i])
        corpus[i] = re.sub(r'[^\w\s]', ' ', corpus[i])
        corpus[i] = corpus[i].lower()
        corpus[i] = re.sub(r'\s{2,}', ' ', corpus[i])
        # corpus[i] = ' '.join([stemmer.stem(x) for x in corpus[i].split()])
    return corpus