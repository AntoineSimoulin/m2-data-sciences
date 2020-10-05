import re

sentences_pattern = re.compile(r"(?<![A-Z]\.)(?<=\.|\?|\!|»)\s", flags=re.M)

def split_into_sentences(text):
    sentences = re.split(sentences_pattern, text)
    return sentences

print('A la recherche du temps perdu')
print('-' * len('A la recherche du temps perdu'), '\n')
    
for s in split_into_sentences(paragraphes_all[0]):
    print(s, '\n')
    
# Pour la première phrase des Misérables 
miserables_first_sentence = "En 1815, M. Charles-François-Bienvenu Myriel était évêque de Digne. C’était un vieillard d’environ soixante-quinze ans ; il occupait le siège de Digne depuis 1806. Quoique ce détail ne touche en aucune manière au fond même de ce que nous avons à raconter, il n’est peut-être pas inutile, ne fût-ce que pour être exact en tout, d’indiquer ici les bruits et les propos qui avaient couru sur son compte au moment où il était arrivé dans le diocèse. "

print('Les misérables')
print('-' * len('Les misérables'), '\n')

for s in split_into_sentences(miserables_first_sentence):
    print(s, '\n')