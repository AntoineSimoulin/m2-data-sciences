df = {
    'je': 1,
    'aime': 1,
    'pas': 1,
    'les': 2,
    'livres': 1,
    'un': 2,
    'livre': 2,
    'très': 1,
    'complet': 1,
    'clairement': 1,
    'pour': 1,
    'filles': 1}

n_docs = 3
tf_je = 1
print(round(tf_je * (np.log(n_docs / df['je']) + 1), 4))

tfidf_vec = TfidfVectorizer(use_idf=True, smooth_idf=False, norm=None)
tfidf_vec.fit(docs)
tfidf_vec.transform(docs).toarray()

list(zip(tfidf_vec.get_feature_names(), tfidf_vec.transform([docs[2]]).toarray()[0]))