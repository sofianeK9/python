# exo 10.2
# Créer une fonction nommée `my_diff()` qui :
# - prend deux paramètres de type `int`
# - soustrait `b` de `a`
# - renvoie le résultat de type `int`
# Notez bien le type hinting dans la déclaration de la fonction
# Appelez la fonction et affichez le résultat

# réponse 10.2

def my_diff(a: int, b: int):
    return a - b

resultat = my_diff(9, 6)
print(resultat)