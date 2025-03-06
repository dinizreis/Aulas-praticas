# Lista Em Python, sao estruturas de dados para armazenar 'listas de informações' dentro de uma única variavel. as Listas são multaveis que permite mudanças []

#___________________________________________________________________________________________________________________

# uma lista é criada usando os []
Lista_de_supermercado = ["Arroz", "Feijao", "Carne", "Frango", "Pao","Icetea", "Arroz", "Arroz", "Carne"]      # aqui eu tenho uma lista de mercado
Lista_de_supermercado [5] = "Refrigerante"      # aqui eu troquei o ultimo item da lista usando esse comando
print(Lista_de_supermercado)         # aqui eu exibo a minha lista com a troca de item feita.

# POsso alterar a lista colocando numeros tambem, posso pegar um item da lista e altera por um numero. 

#____________________________________________________________________________________________________________________

# posso inserir uma lista dentro de outra lista
lista_de_bebidas = ["Heineken", "Campari", "Vinho","Wisky"]     # Aqui tenho uma outra Lista que vou inseri-la dentro da primeira lista.
Lista_de_supermercado.extend(lista_de_bebidas)  # com esse comando " exten() " eu insiro uma lista dentro de outra lista

print(Lista_de_supermercado)    # usando o printe para mostrar no cosole a alteracao.
Lista_de_supermercado.append("Pizzaa")  # Com esse comando .append() eu posso adicionar um item na nossa lista
print(Lista_de_supermercado)
Lista_de_supermercado.insert(1,"Cebola")    # aqui no comando .insert() eu vou inserir um elemento na posiao 1 que no caso esta o feijao 
                                            # e vai empurrar os demais itens da lista pra frente.
print(Lista_de_supermercado)

Lista_de_supermercado.remove("Pao")     # o comando .remove() eu posso usar para remover o item da lista. No exemplo eu removi o pao.
print(Lista_de_supermercado)

Lista_de_supermercado.pop()     # o comando .pop() serve para apagar o ultimo intem da lista.
print(Lista_de_supermercado)

print(Lista_de_supermercado.index("Frango"))    # o comando .index() usado dessa maneira dentro do comando print() me retorna 
                                                # a posicao do meu item na lista. Lembrando que a lista comeca a contar apartir do zero ( 0 )

print(Lista_de_supermercado.count("Arroz")) # o comando .count() me ajuda a contar quantos intens igual exitem na lista.

Lista_de_supermercado.sort()    # Comando .sort() ele vai colocar em ordem alfabetica os intens da minha lista.
print(Lista_de_supermercado)

#______________________________________________________________________________________________________________

# LISTAS BIDIMENSSIONAIS

# AQUI VOU CRIAR UMA LISTA DE NUMEROS. 
# eu quero que os numeros 1 2 3 fiquem em uma lista e os numeros 4 5 6 em outra lista e 7 8 9 em outra lista

# segue o exemplo a baixo

tabela_de_numeros = [[1,2,3],[4,5,6],[7,8,9],[0]]   # aqui eu tenho quatro listas diferentes dentro de uma lista

# print(tabela_de_numeros[0][1])

for linha in tabela_de_numeros:
    print(linha)
    for col in linha:   # dentro do 'for' eu posso criar outro 'for'. e esse 'for' eh para exibir uma coluna
        print(col)