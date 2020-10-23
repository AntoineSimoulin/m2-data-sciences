def most_similar(query, word2vec_embeddings, w2idx, idx2w, topn=10):
    query_idx = w2idx.get(query, 0)
    query_emb = word2vec_embeddings[query_idx]
    cosines = np.dot(word2vec_embeddings, query_emb)

    # on récupèree les 10 valeurs les plus élelvées
    idxs = np.argsort(cosines)[::-1][1:topn + 1]

    # on renvoie les mots correspondants
    return [(idx2w[idx], cosines[idx]) for idx in idxs]
