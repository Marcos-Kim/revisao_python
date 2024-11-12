numeros =[]
for x in range(0,5):
    s = int(input("Informe o valor: "))
    numeros.append(s)

m = numeros[0]
for x in numeros:
    if x > m:
        m = x
print("o maior valor é "+str(m))