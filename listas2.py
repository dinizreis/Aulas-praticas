# PEDINDO UMA LISTA PARA O USUARIO

# ________________________________________________________________

# primeira solucao

# tamanho = int(input("Digite o tamanho da lista"))

# lista = []
# for i in range(tamanho):
#     num = int(input(f"Digite o {tamanho} numero: ".format(i+1)))
#     lista.append(num)

#_________________________________________________________________________

# segunda solucao

lista_para_numeros = input("Digite a lista de numeros  obs: separe com (, ou  'espaco' ): ")
numeros = lista_para_numeros.split(", ")
print(numeros)  # imprimir os numeros
print(type(numeros[0]))     # imprimir o tipo do primeiro intem da lista

for i in range(len(numeros)):
    numeros[i] = int(numeros[i])

print(numeros)
print(type(numeros[0]))