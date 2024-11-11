turno = input("Digite seu turno: M para matutino, V para vespertino ou N para noturno: ")
turno = turno.upper()

if turno == "M":
    print ("Bom dia.")
elif turno == "V":
    print ("Boa tarde.")
elif turno == "N":
    print ("Boa noite.")
else:
    print ("Valor inválido.")