# exo 3.9
# Charly fait ses courses.
# Il compare le prix de deux marques différentes de chocolat.
# La marque Alpha propose une tablette à 2,00 euros (pour 120 g).
# La marque Beta propose une tablette à 1,70 euros (pour 100 g).
# Charly a l'intuition que la marque Alpha est plus avantageuse.
# A-t-il raison ?
# Calculez d'abord le poid au kilo (convertir les grammes en kilo donc) et stockez les résultats dans les variables `weight_alpha` et `weight_beta`.
# Puis calculez le prix au kilo avec les variables `price_alpha` et `weight_alpha`, et `price_beta` et `weight_beta` respectivement puis stockez les résultat dans les variables `price_per_kilo_alpha` et `price_per_kilo_beta`.
# Utilisez un opérateur de comparaison (qui doit donc renvoyer une valeur booléenne) pour vérifier si Charly a raison.
# Affichez le résultat booléen.

price_alpha = 2.00
price_beta = 1.70

# réponse 3.9
weight_alpha = 120 / 1000
print(weight_alpha)

weight_beta = 170 / 1000
print(weight_beta)


price_alpha = 1000 / 120 * 2
print(price_alpha)

price_beta = 1000 / 170 *1.7
print (price_beta)

print(price_alpha < price_beta)

text1 = "lorem ipsum"
result = "e" in text1
print(result)

e = random.randint(0, 100)
f = random.randint(0, 100)
print(f'{e=}')
print(f'{f=}')