age = int(input("Digite a sua idade: "))

if age < 4:
    print("Entrada gratuita")
elif age >= 4 and age < 18:
    print ("Ingresso R$ 5,00")
elif age >=18 and age < 65:
    print ("Ingresso R$ 10,00")
else:
    print ("Ingresso R$ 5,00")