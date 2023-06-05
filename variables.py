# nombre entier, integer
number1 = 123
number1 = 42
print (number1)

# nombre à virgule flottante, float
number2 = 3.14
print (number2)

#chaine de caractéres

text1 ="foo bar baz"
print (text1)

#booléen, boolean
python_is_cool = True
print (python_is_cool)

python_is_boring = False
print(python_is_boring)

#valeur nulle, null value
user_accepted_terms = None
print (None)

# types de données (permet de connaitre quel est le type de données)
print (type (number1))
print (type (number2))
print (type (text1))
print (type (python_is_cool))
print (type (python_is_boring))
print (type (user_accepted_terms))



# interroger le type des autres variables

# transtypage int -> str
print (type(str(number1)))
print(str(number1))

# transtypage int ->bool
print(type(bool(number1)))
print(bool(number1))

# convertir en booléen, la valeur 0 donne false
number3 = 0
print(bool(number3))

# transtypage str ->int
print(type(int(text1)))

text3 ="123456789"
print(type(int(text3)))

# les fonctions de transtypage
# str() convertir vers string chaine de caractére
# int() convertir vers integer nombre entier
# float() convertir float nombre à virgule
# bool() convertir vers boolean

