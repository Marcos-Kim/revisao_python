salario = float(input("Digite o seu salário: "))

valor_aumento = 0
novo_salario = 0

if salario <= 280:
    valor_aumento = salario * 20/100
    novo_salario = salario + valor_aumento
    print ("O seu salário atual é "+str(salario)+" 20% de aumento. O valor do aumento é "+str(valor_aumento)+" e o novo salário é "+str(novo_salario))

elif salario < 700:
    valor_aumento = salario * 15/100
    novo_salario = salario + valor_aumento
    print ("O seu salario atual é "+str(salario)+" 15% de aumento. O valor do aumento é "+str(valor_aumento)+" e o novo salário é "+str(novo_salario))

elif salario < 1500:
    valor_aumento = salario * 10/100
    novo_salario = salario + valor_aumento
    print ("O seu salario atual é "+str(salario)+" 10% de aumento. O valor do aumento é "+str(valor_aumento)+" e o novo salário é "+str(novo_salario))

else:
    valor_aumento = salario * 5/100
    novo_salario = salario + valor_aumento
    print ("O seu salario atual é "+str(salario)+" 5% de aumento. O valor do aumento é "+str(valor_aumento)+" e o novo salário é "+str(novo_salario))