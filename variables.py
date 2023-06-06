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



text3 ="123456789"
print(type(int(text3)))

# les fonctions de transtypage
# str() convertir vers string chaine de caractére
# int() convertir vers integer nombre entier
# float() convertir float nombre à virgule
# bool() convertir vers boolean

# string 
# """" pour ecrire un long texte et permet d'utiliser des sauts de lignes

text4 =""" <div>
    <h1>Titre du premier niveau</h1>
</div>"""

print(text4)

#\n est equivalent à un saut à la ligne
#\t est equivalent à une tabulation

text5 = "<div>\n    <h1> Titre de premier niveau</h1>\n </div>\n"

print (text5)

#\" est equivalent à une guillemment"
#\\ est equivalent à un back slash \

text6 = "Foo \"Bar\"Baz"
text7 = "C:\\Program Files\\Foo"

print (text6)
print (text7)

# permutez les deux variables a et b en utilisant les operateurs d'affectations et le nom des variables
a = 123
d = 42

# permutation des valeurs à l'aide d'une variable temporaire
c = b
b = a
a = c


print (a)
print (b)

# permutations des valeurs à l'aide d'operations arithmetiques

a = a + b
b = a - b
a = a - b

print (a)
print (b)
