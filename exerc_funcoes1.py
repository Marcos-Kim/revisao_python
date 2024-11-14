# Exercício 1:
def soma (a,b):
    return a+b


# Exercício 2:
def celsius_fahrenheit(c):
   c = float(c)
   f = float((9 * c) / 5) + 32

  # return 'A temperatura em fahrenheit: {0}°F'.format(f)
   return "A temperatura em Fahrenheit é: "+str(f)+"°F" # + significa concatenação


# Exercício 3:
def par_impar (n):
    if n % 2 == 0:
        print("O número é par.")
    else:
        print("O número é ímpar.")


# Exercício 4:
def string_invertida (texto):
    # string_invertida = ''.join(reversed(texto))
    # print(string_invertida)
    tamanho_do_texto = len(texto)
    for i in range(tamanho_do_texto-1,-1,-1): # o primeiro -1 é para indicar em qual posição devemos começar,
        # o segundo -1 é referente à posição e o terceiro -1 é referente à quantidade de casas a andar.
        print(texto[i],end="") # end="" para imprimir horizontalmente.
    print()
    
# Exercício 5:
def verificar_palindromo(palavra):
    palavra = palavra.lower()
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

# def media (lista_numeros):


# Exercício 7:
def pares (lista_numeros):
    lista_pares = []

    for i in lista_numeros:
        if i % 2 == 0:
            lista_pares.append(i)
    return lista_pares