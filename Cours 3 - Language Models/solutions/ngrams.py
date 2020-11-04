def sentence_2_n_grams(sentences, n=3, start_token='<s>', end_token='</s>'):
    ngrams = []
    for s in sentences:
        tokens = [start_token] + s + [end_token]
        ngrams += zip(*[tokens[i:] for i in range(n)])
    return Counter([" ".join(ngram) for ngram in ngrams])