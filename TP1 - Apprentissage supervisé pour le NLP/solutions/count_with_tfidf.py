# solution
tfidf_vec = TfidfVectorizer(vocabulary=cv.vocabulary_, binary=True, use_idf=False, norm=None)
tfidf_vec.fit(docs)
tfidf_vec.transform(docs).toarray()