# Observer l'impact sur la taille du vocabulaire
%%time
X_train_df['tokens_stem'] = X_train_df['tokens'].apply(stemmatize)
X_train_df['tokens_lem'] = X_train_df['reviews'].apply(lemmatize)


tokens = [ll for l in X_train_df.tokens.values for ll in l]
tokens_stem = [ll for l in X_train_df.tokens_stem.values for ll in l]
tokens_lem = [ll for l in X_train_df.tokens_lem.values for ll in l]


vocab_initial = np.unique(tokens)
vocab_stem = np.unique(tokens_stem)
vocab_lem = np.unique(tokens_lem)

label_init  = "Vocabulaire initial : " + str(len(vocab_initial))
label_stem = "Vocabulaire apres stemmatisation : " + str(len(vocab_stem))
label_lem = "Vocabulaire apres lemmatization : " + str(len(vocab_lem))

fig, ax = plt.subplots(figsize=(20, 8))

ax.bar([1,2,3], [len(vocab_initial), len(vocab_stem), len(vocab_lem)], color='#970137', alpha=0.8, linewidth=15)

# set labels
ax.set_ylabel('Taille du vocabulaire', fontsize=15,
              fontweight='black', color='#333F4B')
ax.set_xlabel('')
ax.set_title('Impact des prétraitements sur la taille du vocabulaire')

# set axis
plt.xticks([])

#set annotation
plt.annotate(label_init, (1, len(vocab_initial)), textcoords="offset points",
                 xytext=(1, -40 - len(label)), ha='center',
                 fontsize=15,  weight='bold', color='white')
plt.annotate(label_stem , (2, len(vocab_stem)), textcoords="offset points",
                 xytext=(1, -40 - len(label)), ha='center',
                 fontsize=15,  weight='bold', color='white')
plt.annotate(label_lem , (3, len(vocab_lem)), textcoords="offset points",
                 xytext=(1, -40 - len(label)), ha='center',
                 fontsize=15,  weight='bold', color='white')
plt.show();

# tokenized_corpus_flatten = [ll for l in X_valid_df['tokens'].values for ll in l]
# tokens_counter = Counter(tokenized_corpus_flatten)
#
# print("Validation set contains {} unique words.".format(len(tokens_counter)))
#
# n_tokens = sum([len(t) for t in X_valid_df['tokens'].values])
# print("Validation set contains {:,d} tokens.".format(n_tokens))
#
# assert len(tokenized_corpus_flatten) == n_tokens
#
# X_valid_df['tokens_stem'] = X_valid_df['tokens'].apply(stemmatize)
#
# tokenized_corpus_flatten = [ll for l in X_valid_df['tokens_stem'].values for ll in l]
# tokens_counter = Counter(tokenized_corpus_flatten)
#
# n_tokens = sum([len(t) for t in X_valid_df['tokens_stem'].values])
# print("Validation set contains {:,d} tokens.".format(n_tokens))
#
# print("Validation set contains {} unique words.".format(len(tokens_counter)))
#
#
# # X_valid_df['tokens'] = X_valid_df['reviews'].apply(lambda x: [lemmatize(t) for t in x])
#
# # tokenized_corpus_flatten = [ll for l in X_valid_df['tokens'].values for ll in l]
# # tokens_counter = Counter(tokenized_corpus_flatten)
#
# # n_tokens = sum([len(t) for t in X_valid_df['tokens'].values])
# # print("Validation set contains {:,d} tokens.".format(n_tokens))
#
# # print("Validation set contains {} unique words.".format(len(tokens_counter)))