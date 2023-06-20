# exo 6.15
# Trouvez la chaîne de caractères la plus longue dans une liste.
# Affichez son index, sa valeur et sa longueur.
#
# ATTENTION : ne pas utiliser la fonction list.index()
# ATTENTION : cet exercice nécessite l'utilisation d'une boucle `for`

my_list = ['Lorem', 'ipsum', 'dolor', 'sit', 'amet', 'consectetur', 'adipiscing', 'elit']

# réponse 6.15

i = 0
chaine_plus_longue = ""
for i in my_list:
    if i isinstance(i, str) and len(i) > len(chaine_plus_longue):
        chaine_plus_longue = i
        print(chaine_plus_longue)
