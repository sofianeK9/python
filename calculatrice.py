# on demande à la personne de saisir deux nombres et une opération
number1 = float(input("saisir le premier nombre: "))
number2 = float(input("saisir le deuxiéme nombre: "))
operation = input("saisir votre operation: (+ - / *):")


if operation == "+":
    print ( number1 + number2)
elif operation == "-":
    print( number1 - number2)
    
elif operation == "/":
    print(number1 / number2)
    
elif operation == "*":
    print(number1 * number2)
else:
    print("ERREUR de saisie")
    
