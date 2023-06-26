# exo 10.5
# Créer une fonction nommée `compare()` qui :
# - prend deux paramètres `a` et `b` de type `float`
# - renvoie une valeur de type `int`
# - renvoie 1 si `a` est plus grand que `b`
# - renvoie -1 si `a` est plus petit que `b`
# - renvoie 0 si `a` et `b` sont égaux
# Appelez la fonction et affichez le résultat

# réponse 10.5

def compare(a: float, b: float) -> float:
   if a > b:
       return int(1)
   elif a < b:
       return int (-1)
   else:
       return int(0)
   
   
resultat = compare(1.9, 1.1)
print(resultat)