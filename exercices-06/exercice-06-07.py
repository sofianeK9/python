# exo 6.7
# Inversez la position des valeurs `bar` et `lorem` puis affichez le résultat
#
# ATTENTION : Dans l'énoncé, quand il est écrit Xème position, cela correspond à l'index X-1

my_list = ['foo', 'bar', 'baz', 'lorem', 'ipsum']

# réponse 6.7

# index1 = my_list.index('bar')
# print(index1)
# index2 = my_list.index('lorem')
# print(index2)

my_list[1],my_list[3] = my_list[3],my_list[1]
print(my_list)