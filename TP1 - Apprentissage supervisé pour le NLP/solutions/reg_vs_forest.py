
# Modèle de régression logistique
logreg = LogisticRegression(penalty='l2', C=1.0)

logreg.fit(X_train_tfidf, y_train)

y_logreg_pred = logreg.predict(X_valid_tfidf)
y_logreg_pred = pd.DataFrame(y_logreg_pred)


# Modèle de forêt aléatoire
rf = RandomForestClassifier(n_estimators=500,
                            max_depth = 20
                           )

rf.fit(X_train_tfidf, y_train)

y_rf_pred = rf.predict(X_valid_tfidf)
y_rf_pred = pd.DataFrame(y_rf_pred)


# Comparaison des performances
print("Matrice de confusion de la régression logistique : ")
print(confusion_matrix(y_valid, y_logreg_pred))
print("Score de précision de la régression logisitique : "+str(round(precision_score(y_valid, y_logreg_pred)*100,2)))
print("Score de rappel de la régression logisitique : "+str(round(recall_score(y_valid, y_logreg_pred)*100,2)))
print("Score F1 de la régression logisitique : "+str(round(f1_score(y_valid, y_logreg_pred)*100,2)))
print()
print("Matrice de confusion de la forêt aléatoire : ")
print(confusion_matrix(y_valid, y_rf_pred))
print("Score de précision de la forêt aléatoire : "+str(round(precision_score(y_valid, y_rf_pred)*100,2)))
print("Score de rappel de la forêt aléatoire : "+str(round(recall_score(y_valid, y_rf_pred)*100,2)))
print("Score F1 de la régression forêt aléatoire : "+str(round(f1_score(y_valid, y_rf_pred)*100,2)))