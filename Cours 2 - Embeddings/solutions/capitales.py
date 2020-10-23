word_emb_tsne = TSNE(perplexity=30).fit_transform(word2vec_embeddings[:10000])

plt.figure(figsize=(10, 10))
axis = plt.gca()
np.set_printoptions(suppress=True)

pays = ['Allemagne', 'France', 'Belgique', 'Madrid', 'Londres']
capitales = ['Berlin', 'Paris', 'Bruxelles', 'Espagne', 'Angleterre']

x = [word_emb_tsne[w2idx[w], 0] for w in pays] + [word_emb_tsne[w2idx[w], 0] for w in capitales]
y = [word_emb_tsne[w2idx[w], 1] for w in pays] + [word_emb_tsne[w2idx[w], 1] for w in capitales]

plt.scatter(x, y, marker=".", s=1)

for p in pays:
    plt.annotate(p,
                 xy=(word_emb_tsne[w2idx[p], 0], word_emb_tsne[w2idx[p], 1]),
                 xytext=(0, 0), textcoords='offset points')

for c in capitales:
    plt.annotate(c,
                 xy=(word_emb_tsne[w2idx[c], 0], word_emb_tsne[w2idx[c], 1]),
                 xytext=(0, 0), textcoords='offset points')

for c, p in zip(pays, capitales):
    plt.annotate("",
                 xy=(word_emb_tsne[w2idx[c], 0], word_emb_tsne[w2idx[c], 1]),
                 xytext=(word_emb_tsne[w2idx[p], 0], word_emb_tsne[w2idx[p], 1]),
                 arrowprops=dict(arrowstyle="->"))

plt.xlim(min(x) - 5, max(x) + 5)
plt.ylim(min(y) - 5, max(y) + 5)
plt.savefig("tsne-pays-capitales.png")
plt.show()