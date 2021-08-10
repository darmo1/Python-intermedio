#Funciones lamda o llamadas anónima , son funciones que no tiene nombre

# lamda argumentos: expresion
#Puede tener varios argumentos pero solo una expresión

palindrome = lambda string : string == string[::-1]
print(palindrome('ana'))

#El equivalente es

def palindromo(string):
    return string == string[::-1]

print(palindromo('ana'))