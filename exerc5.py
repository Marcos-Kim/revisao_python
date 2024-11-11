n1 = int(input("Digite um número: "))
n2 = int (input ("Digite outro número: "))
n3 = int (input ("Digite mais um número: "))

if n1 > n2 and n1 > n3:
    print (n1, "é o maior número dentre os 3 digitados.")
elif n2 > n1 and n2 > n3:
    print (n2, "é o maior número dentre os 3 digitados.")
elif n3 > n1 and n3 > n2:
    print(n3, "é o maior número dentre os 3 digitados.")
# elif n1 == n2 == n3:
  #  print("Os números são iguais.")
else:
    print("Os números são iguais.")