# exo 6.14
# Créez une deuxième liste nommée `new_list` ne contenant que les nombres entiers de la liste
#
# ATTENTION : cet exercice nécessite l'utilisation d'une boucle `for`

my_list = [2.71, 42, 123, 2, 3.14, 1.61]

# réponse 6.14
new_list =[]
i = 0
for i in my_list:
    if isinstance(i, int):
        new_list.append(i)

    print(new_list)