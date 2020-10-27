
def vectorize(tokens):
    vectors = np.array([w2v_model[t] for t in tokens if t in w2v_model.vocab])
    if len(vectors):
        vectors_sum = np.sum(vectors, axis=0)
    else:
        vectors_sum = np.zeros_like(w2v_model['roi'])
    return vectors_sum