class Tokenizer(BaseEstimator, TransformerMixin):

    def __init__(self, tokenizer_pattern=r"(?:[a-zA-ZÀ-ÖØ-ö0-9])+'?",
                 do_lemmatization=False,
                 do_stemmatization=False):

        # self.token_pattern = re.compile(tokenizer_pattern)
        self.do_stemmatization = do_stemmatization
        self.do_lemmatization = do_lemmatization
        if self.do_stemmatization:
            self.stemmer = FrenchStemmer()

        if self.do_lemmatization:
            self.nlp = spacy.load('fr_core_news_md')
            self.nlp.tokenizer = self.custom_tokenizer

    def _custom_tokenizer(self, text):
        tokens = self._tokenize(text)
        return Doc(nlp.vocab, tokens)

    def _lemmatize(self, text):
        doc = self.nlp(X_train_df.loc[0, 'reviews'])
        return [token.lemma_ for token in doc]

    def _stemmatize(self, tokens):
        return [self.stemmer.stem(t) for t in tokens]

    def _tokenize(self, text):
        tokens = re.findall(r"(?:[a-zA-ZÀ-ÖØ-ö0-9])+'?", text)  # self.token_pattern
        tokens = [t for t in tokens]
        return tokens

    def fit(self, X, y=None):
        return self

    def transform(self, X, y=None):
        if isinstance(X, pd.DataFrame):
            X = X.copy()
        else:
            if not isinstance(X, list):
                X = [X]

        if self.do_lemmatization:
            if isinstance(X, pd.DataFrame):
                X["tokens"] = X["reviews"].apply(self._lemmatize)
            else:
                tokens = [self._lemmatize(x) for x in X]
        else:
            if isinstance(X, pd.DataFrame):
                X["tokens"] = X["reviews"].apply(self._tokenize)
            else:
                tokens = [self._tokenize(x) for x in X]
        if self.do_stemmatization:
            if isinstance(X, pd.DataFrame):
                X["tokens"] = X["tokens"].apply(self._stemmatize)
            else:
                tokens = [self._stemmatize(x) for x in X]
        if isinstance(X, pd.DataFrame):
            return X["tokens"]
        else:
            return tokens