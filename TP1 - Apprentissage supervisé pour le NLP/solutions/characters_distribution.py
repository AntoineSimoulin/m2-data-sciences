# compter les caractères dans corpus
character_counts = Counter(" ".join(X_train_df['reviews'].tolist()))

print("Most common characters in corpus : ")
print(character_counts.most_common(10))

print("\nNumber of characters in the dataset: {}.".format(len(character_counts)))