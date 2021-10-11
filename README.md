
# Cours de M2 Data Sciences

Ce cours fait partie du Master 2 Mathématiques et Informatique pour la Data Science ([M2 MIDS](https://m2mids.github.io/m2mids/)) de l'université de Paris. Le cours introduit les méthodes statistiques de Traitement Automatique de la Langue Naturelle. Les méthodes de Deep Learning ne sont abordées que dans des cours ultérieurs.

## Calendrier

Le calendrier des séances est décrit ci-dessous.

| Séance | Thèmes | TP / Exercises | Slides |
|:---:|---|:---:|:---:|
| Cours **#1** |  Modélisation statistique du langage, vectorisation de texte | [![Open In Colab](https://colab.research.google.com/assets/colab-badge.svg)](https://colab.research.google.com/github/AntoineSimoulin/m2-data-sciences/blob/master/Cours%201%20-%20Mod%C3%A9lisation%20statistique%20du%20langage/Fr%C3%A9quences%20des%20mots.ipynb) <a download="Cours%201%20-%20Mod%C3%A9lisation%20statistique%20du%20langage/Fr%C3%A9quences%20des%20mots.ipynb" href="https://github.com/AntoineSimoulin/m2-data-sciences/raw/master/Cours%201%20-%20Mod%C3%A9lisation%20statistique%20du%20langage/Fr%C3%A9quences%20des%20mots.ipynb" title="Course1"><img alt="Course1" src="https://www.svgrepo.com/show/349485/python.svg" width="15" height="15"></a> | <a href="https://github.com/AntoineSimoulin/m2-data-sciences/tree/master/Cours%201%20-%20Mod%C3%A9lisation%20statistique%20du%20langage/Cours_1.pdf"> <img src=https://www.svgrepo.com/show/255820/ppt.svg width="15" height="15"></a> |
| TP **#1** | Classification de textes, modèles BoW | [![Open In Colab](https://colab.research.google.com/assets/colab-badge.svg)](https://colab.research.google.com/github/AntoineSimoulin/m2-data-sciences/blob/master/TP1%20-%20Apprentissage%20supervis%C3%A9%20pour%20le%20NLP/Classification.ipynb) <a download="TP1%20-%20Apprentissage%20supervisé%20pour%20le%20NLP/Classification.ipynb" href="https://github.com/AntoineSimoulin/m2-data-sciences/blob/master/TP1%20-%20Apprentissage%20supervis%C3%A9%20pour%20le%20NLP/Classification.ipynb" title="Course1"><img alt="Tp1" src="https://www.svgrepo.com/show/349485/python.svg" width="15" height="15"></a> | |
| TP **#2** | Détection de thèmes, LDA | [![Open In Colab](https://colab.research.google.com/assets/colab-badge.svg)](https://colab.research.google.com/github/AntoineSimoulin/m2-data-sciences/blob/master/TP2%20-%20Text%20Mining/TP2%20-%20Exploration%20de%20topics[COLAB].ipynb)| |
| Cours **#2** | Représentations sémantiques lexicales et sémantique distributionnelle : Embeddings de mots | [![Open In Colab](https://colab.research.google.com/assets/colab-badge.svg)](https://colab.research.google.com/github/AntoineSimoulin/m2-data-sciences/blob/master/Cours%202%20-%20Embeddings/Words%20Embeddings.ipynb)|  <a href="https://github.com/AntoineSimoulin/m2-data-sciences/tree/master/Cours%202%20-%20Embeddings/Cours_2.pdf"> <img src=https://www.svgrepo.com/show/255820/ppt.svg width="15" height="15"></a>  |
| TP **#3** | Embeddings de mots pour l'analyse de sentiments | [![Open In Colab](https://colab.research.google.com/assets/colab-badge.svg)](https://colab.research.google.com/github/AntoineSimoulin/m2-data-sciences/blob/master/TP3%20-%20Word%20Embeddings/EmojiFy[COLAB].ipynb)| |
| Cours **#3** | Modélisation de séquences de mots : modèles de langue. Application à la génération de texte | [![Open In Colab](https://colab.research.google.com/assets/colab-badge.svg)](https://colab.research.google.com/github/AntoineSimoulin/m2-data-sciences/blob/master/Cours%203%20-%20Language%20Models/Mod%C3%A8les%20de%20langues.ipynb) | <a href="https://github.com/AntoineSimoulin/m2-data-sciences/tree/master/Cours%203%20-%20Language%20Models/Cours_3.pdf"> <img src=https://www.svgrepo.com/show/255820/ppt.svg width="15" height="15"></a>  |
| Cours **#4** | Ouverture sur les méthodes de Deep Learning pour le NLP (RNN, Seq2Seq, Attention, Bert) Application au systèmes de Q&A | [![Open In Colab](https://colab.research.google.com/assets/colab-badge.svg)](https://colab.research.google.com/github/AntoineSimoulin/m2-data-sciences/blob/master/Cours%204%20-%20Introduction%20NLP%20%26%20Deep%20Learning/Bert_QA[COLAB].ipynb)|  <a href="https://github.com/AntoineSimoulin/m2-data-sciences/tree/master/Cours%204%20-%20Introduction%20NLP%20%26%20Deep%20Learning/Cours_4.pdf"> <img src=https://www.svgrepo.com/show/255820/ppt.svg width="15" height="15"></a>  |

## Comment l'utiliser ?

### 💻 En local

Si vous souhaitez exécuter le TP sur votre ordinateur, voici une procédure rapide pour installer Python et les librairies requises. Ca évitera d’avoir des problèmes de version de librairies qui interfère avec d’autres cours ou projets. Pour installer Python, je vous conseille d’utiliser [Anaconda](https://www.anaconda.com/products/individual) (~450 MB). Sélectionnez l’installation correspondent à votre système d’exploitation et “64-Bit Graphical Installer” puis suivez les instructions pour installer Anaconda.

Pour les librairies, je vous conseille de créer un environnement virtuel python pour l’ensemble du cours. Ouvrez un terminal et tapez la commande suivante :

```bash
conda create -n nlp-101 python=3.6
# Vous pouvez activer l’environnement avec la commande suivante
conda activate nlp-101
```

Si vous utilisez [jupyter-lab](https://jupyterlab.readthedocs.io/en/stable/), vous pouvez répertorier l’environement :

```bash
conda install ipykernel
ipython kernel install --user --name='nlp-101'
```

Nous allons installer les librairies avec le gestionnaire pip. Vérifiez que la version utilisée est bien celle associée à anaconda :
```bash
pip show pip
```
Puis mettez le à jour :
```bash
pip install --upgrade pip
```

Installez les librairies suivantes :
```bash
pip install scikit-learn==0.23.2 matplotlib==3.3.2 pandas==1.1.3 lime==0.2.0.1 unidecode==1.3.2 umap-learn==0.4.6 umap-learn[plot] nltk==3.5 spacy==2.3.2
pip install --upgrade jupyter
```

Vous pouvez vérifier que chaque package est bien installé avec la commande :
```bash
python -c "import sklearn; print(sklearn.__version__)"
```

Finalement téléchargez le modèle Spacy français :
```bash
python3 -m spacy download fr_core_news_md
```

### ☁️ Google Colab

Si vous disposez d'un compte Google, vous pouvez également éxécuter l'ensemble des TPs et exercices sur l'interface [Google Colab](https://colab.research.google.com/).

### 🐳 Docker

Il est également possible de faire tourner un serveur jupyter dans un Docker. L'avantage est que ce dernier tournera dans un environnement virtuel en grande partie indépendant des contraintes de votre machine. Par exemple de votre installation python ou de votre système d'exploitation.

Pour cela, installez [Docker Desktop](https://www.docker.com/products/docker-desktop) (c'est gratuit pour les utilisation non professionnelles). Vous pouvez ensuite cloner le répertoire et construire l'image Docker. Pour cela ouvrez un terminal et exécuter les commandeds suivantes :

```bash
git clone git@github.com:AntoineSimoulin/m2-data-sciences.git
cd m2-data-sciences
git pull
docker build -t m2-data-sciences .
docker run -p 8888:8888 m2-data-sciences
```
