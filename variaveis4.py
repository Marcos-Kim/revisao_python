alimentos = ["Maçã","Arroz","Feijão"]
categoria = ("Grãos","Frutas","Legumes")
pessoa = {"Nome":"Paula","Idade":"38","Altura":"1.65"}

print (alimentos)
print (type(alimentos))
print (len(alimentos))
# Adicionar mais um elemento
alimentos.append ("Macarrão")
print (len(alimentos))

print (categoria)
print (type(categoria))
print (len(categoria))

print (pessoa)
print (type(pessoa))
print (len(pessoa))
# Adicionar um item a pessoa.
# Adicionar uma nova chave com o seu respectivo valor.
# Está sendo adicionado a chave email com o valor email da pessoa
pessoa["email"]="paula@gmail.com"
print (pessoa)
print (len(pessoa))