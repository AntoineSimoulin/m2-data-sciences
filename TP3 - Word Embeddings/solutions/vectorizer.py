class Vectorizer(BaseEstimator, TransformerMixin):

    def __init__(self, agg_method='mean', normalize=False):
        self.agg_method = agg_method
        self.normalize = normalize
        self.tfidf_vectorizer = TfidfVectorizer(tokenizer=lambda x: x,
                                                lowercase=False,
                                                token_pattern=None)

    def vectorize(self, tokens):

        vectors = np.array([w2v_model[t] for t in tokens if t in w2v_model.vocab])

        if len(vectors) == 0:
            sentence_embedding = np.zeros_like(w2v_model['roi'])
        elif len(vectors) == 1:
            sentence_embedding = np.squeeze(vectors)
        elif len(vectors) > 1:
            if self.agg_method == 'mean':
                sentence_embedding = np.mean(vectors, axis=0)
            elif self.agg_method == 'max':
                sentence_embedding = np.max(vectors, axis=0)
            elif self.agg_method == 'sum':
                sentence_embedding = np.sum(vectors, axis=0)
            elif self.agg_method == 'tfidf':
                tf_idf_w = self.tfidf_vectorizer.transform([tokens]).todense().transpose()
                tf_idf_w = np.squeeze([tf_idf_w[self.w2idx_tfidf.get(t, 0)] for t in tokens if t in w2v_model.vocab])
                sentence_embedding = np.average(vectors, weights=tf_idf_w, axis=0)

        return sentence_embedding

    def _vectorize(self, tokens):
        return vectorize(tokens)

    def fit(self, X, y=None):
        self.tfidf_vectorizer.fit(X['tokens'])
        self.w2idx_tfidf = {w: idx for (idx, w) in enumerate(self.tfidf_vectorizer.get_feature_names())}
        self.idx_tfidf2w = {idx: w for (idx, w) in enumerate(self.tfidf_vectorizer.get_feature_names())}
        return self

    def transform(self, X, y=None, eps=1e-12):
        X = [self.vectorize(t) for t in X['tokens']]
        X = np.array(X)

        if self.normalize:
            X = X / np.linalg.norm(X + eps, axis=1, keepdims=True)
        return X