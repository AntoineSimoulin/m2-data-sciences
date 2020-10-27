vec = CountVectorizer(max_features=10000)
bag_of_word = vec.fit_transform(X_train_df['reviews'])

sum_words = bag_of_word.sum(axis=0)
word_freq = {word: sum_words[0, idx] for word, idx in vec.vocabulary_.items()}
word_freq_sorted = [(word, sum_words[0, idx]) for word, idx in vec.vocabulary_.items()]
word_freq_sorted = sorted(word_freq_sorted, key=lambda x: x[1], reverse=True)
word_freq_sorted = [x[0] for x in word_freq_sorted]

for word in ['je', 'le', 'livres', 'oeuvre']:
    print("frequence d'occurence de \'%s\' : %i" % (word, word_freq[word]))
    print("top fréquence de \'%s\' : %i" % (word, word_freq_sorted.index(word)))

vec = TfidfVectorizer()
vec.fit(X_train_df['reviews'])
word_idf = {word: vec.idf_[idx] for word, idx in vec.vocabulary_.items()}

for word in ['je', 'le', 'livres', 'oeuvre']:
    print("idf de \'%s\' : %f" % (word, word_idf[word]))

vec = TfidfVectorizer(max_df=0.2)
vec.fit(X_train_df['reviews'])
word_idf = {word: vec.idf_[idx] for word, idx in vec.vocabulary_.items()}

for word in ['je', 'le', 'livres', 'oeuvre']:
    print("%s in voc :" % word, word in word_idf)