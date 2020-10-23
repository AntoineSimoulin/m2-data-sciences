plt.figure(figsize=(10, 10))
axis = plt.gca()
np.set_printoptions(suppress=True)

infinitif = ['manger', 'lancer', 'jouer', 'cuisiner', 'sortir']
conjugaison = ['mange', 'lance', 'joue', 'cuisine', 'sors']

x = [word_emb_tsne[w2idx[w], 0] for w in infinitif] + [word_emb_tsne[w2idx[w], 0] for w in conjugaison]
y = [word_emb_tsne[w2idx[w], 1] for w in infinitif] + [word_emb_tsne[w2idx[w], 1] for w in conjugaison]

plt.scatter(x, y, marker=".", s=1)

for i in infinitif:
    plt.annotate(i,
                 xy=(word_emb_tsne[w2idx[i], 0], word_emb_tsne[w2idx[i], 1]),
                 xytext=(0, 0), textcoords='offset points')

for c in conjugaison:
    plt.annotate(c,
                 xy=(word_emb_tsne[w2idx[c], 0], word_emb_tsne[w2idx[c], 1]),
                 xytext=(0, 0), textcoords='offset points')

for i, c in zip(infinitif, conjugaison):
    plt.annotate("",
                 xy=(word_emb_tsne[w2idx[c], 0], word_emb_tsne[w2idx[c], 1]),
                 xytext=(word_emb_tsne[w2idx[i], 0], word_emb_tsne[w2idx[i], 1]),
                 arrowprops=dict(arrowstyle="->"))

plt.xlim(min(x) - 5, max(x) + 5)
plt.ylim(min(y) - 5, max(y) + 5)
plt.savefig("tsne-pays-capitales.png")
plt.show()