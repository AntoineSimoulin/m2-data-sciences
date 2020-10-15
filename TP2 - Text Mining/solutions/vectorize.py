
# Initialise the count vectorizer
count_vectorizer = CountVectorizer(max_features=2000,
                                   stop_words=STOP_WORDS,
                                   max_df=0.9,
                                   min_df=20)

count_data = count_vectorizer.fit_transform(clean_corpus_split)