def vectorize(tokens):
    vectors = np.array([w2v_model[t] for t in tokens if t in w2v_model.vocab])

    tf_idf_w = tfidf_vectorizer.transform([tokens]).todense().transpose()
    tf_idf_w = np.squeeze([tf_idf_w[w2idx_tfidf[t]] for t in tokens if t in w2v_model.vocab])

    if len(vectors) == 0:
        vectors_sum = np.zeros_like(w2v_model['roi'])
    elif len(vectors) == 1:
        vectors_sum = np.squeeze(vectors * tf_idf_w)
    else:
        vectors_sum = np.average(vectors, weights=tf_idf_w, axis=0)

    return vectors_sum