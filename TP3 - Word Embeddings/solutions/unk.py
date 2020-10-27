def unk_words(tokens):
    unk_words = [1 if t not in w2v_model.vocab else 0 for t in tokens]
    return sum(unk_words), len(unk_words)

unk = [unk_words(t) for t in dataset['tokens']]

unk = sum([u[0] for u in unk]) / sum([u[1] for u in unk]) * 100

print('{:.2f}% tokens are not in the W2V vocabulary.'.format(unk))