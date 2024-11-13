# Exercício 1:
def soma (a,b):
    return a+b


# Exercício 2:
def celsius_fahrenheit(c):
   c = float(c)
   f = float((9 * c) / 5) + 32

   return ('A temperatura em fahrenheit: {0}°F'.format(f))


# Exercício 3:
def par_impar (n):
    resto = n % 2
    if resto == 0:
        print("O número é par.")
    else:
        print("O número é ímpar.")


# Exercício 4:
def string_invertida (string):
    string_invertida = ''.join(reversed(string))
    print(string_invertida)
   

# Exercício 5:
def verificar_palindromo(palavra):
    palavra_invertida = palavra[::-1]
    if palavra == palavra_invertida:
        return ("A palavra é um palíndromo.")
    else:
        return ("A palavra não é um palíndromo.")
       

# Exercício 6:
def media (*numeros):
    numeros = [*numeros]
    soma = sum(*numeros)
    media = soma / len(*numeros)
    print("A média dos números é:", media)


# Exercício 7:
def pares (lista1):
    lista1 = []
    lista2 = []

    for lista2 in lista1:
        if lista1 % 2 == 0:
            print(lista2)