numeros = []
for x in range(0,5):
    n = int(input("Digite um valor: "))
    numeros.append(n)
#exibir os numeros adicionados
print(numeros)
 
#variavel da soma
soma = 0
for i in numeros:
    soma += i
# exibir a soma
print(" A soma dos valores é: "+str(soma))
 
print("A média dos valores é: "+str(soma/len(numeros)))