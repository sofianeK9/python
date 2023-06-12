# import du module random (pour les nombres aléatoires)
import random



# arithmetique
a = 42 + 123
a = 42 - 123
a = 42 * 123
a = 42 / 123

# division entiére, integer division

a = 42 // 123
print(a)

# modulo ou reste de la division (euclidienne)
# pas divisible par 2 donc il est impair
a = 53
print(a % 2)

b =74
print (a % 2)

# puissance, exponentiation
a = 2 ** 3
print (a)

# opérateurs de comparaison
#egalité
result = 123 == 123
print(result)

password = "abc"
user_input ="def"
print(password == user_input)

# plus grand que 
print(123 > 42)

# different de 
print( 123!= 42)

# plus grand ou égal à 
print (123 >= 42)

# plus petit ou egal à
print( 42 <= 42)


# opérateurs composés
b = 0

# incrémentation
# b = b +1
b += 1
b += 1
print(b)

# decrémentation
# l = l -1
l = 2
l -= 1
l -= 1
print(l)

# multiplication
c = 3
# c = c * 2

c *= 2
print (c)

# division

d = 10

# d= d / 3

d /= 3

print(d)

# division entiére

d = 10

# d = d // 3

d //= 3
print(d)

# opérateur d'inclusion
text1 = "Lorem ipsum"

result = "e" in text1

print(result) 

list1 = ['lorem', 'ipsum']
print ("e" in list1)
print("ipsum" in list1)
list1[0]

# comparaison avec des nombres aléatoires
e = random.randint(0, 100)
f = random.randint(0,100)
print(f'{e = }')
print(f'{f = }')

result = e == f
print (result)

result = e < f
print(result)

# expression = element qui peut etre reduit à une valeur

# 1 + 1 -> 2
# (100 + 2)* 31 -> 102 * 3 -> 306
#  1 + 1 > (100 + 2) * 3 -> 2 > 306 -> False
# random.randint (0, 100) -> 100

# pas une expression
# print(100)