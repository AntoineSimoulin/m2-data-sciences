def estimate_probability(word, previous_n_gram,
                         n_gram_counts, n_plus1_gram_counts, vocabulary_size, k=1.0):
    denominator = n_gram_counts.get(previous_n_gram, 0)
    denominator += k * vocabulary_size

    numerator = n_plus1_gram_counts.get(previous_n_gram + ' ' + word, 0)
    numerator += k

    probability = numerator / denominator

    return probability