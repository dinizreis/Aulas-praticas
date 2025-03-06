'''
    Estruturas condiconais aninhadas quer dizer basicamente que eu posso usar varias comdicoes dentro de uma única condicao.

    VAMOS AOS EXEMPLOS!
'''
# --> exemplo 01

nome = str(input("Qual o seu nome? ")).strip()
print("-=-"*20)
if nome == "Higor":
    print("Que nome Bonito!")
print(f"Tenha um bom dia, {nome}!")

'''
    O que aconteceu aqui foi que fizemos uma estrutura de condicao simples.
repara que temos apenas um if e no if está dizendo que se o nome do usuario for igual a um determinado nome
o programa vai emitir uma frase, e se, o usuario não colocar o nome ele vai emitir a oura frasee do print.

é uma condicao simples

'''

nome2 = str(input("Qual o seu nome? ")).strip()
print("-#-" * 20)
if nome2 == "Diniz":
    print("Que maravilhoso nome, voce tem!")
else:
    print("voce tem um nome normal!")
print(f"tenha um bom dia {nome2}")

'''
    Repara que agora usamos basicamente a mesma estrutura de antes, mas com algumas informacoes a mais
temos agora um else: e isso quer dizer que se o programa nao chegar na primeira condicao ele vai cair na condicao do else
e vai emitir aquela frase.

é uma condicao composta

'''

carro = str(input("Qual o seu nome? ")).strip()
print("-#-" * 20)
if carro == "Jetta":
    print("Que magnifico Carro, voce tem!")
elif carro == "Gol" or carro == "corsa" or carro == "Fusca":
    print("Voce tem um Carro muito popular")
else:
    print("voce tem um Carro diferente!")
print(f"Ande devagar com o seu {carro}")

'''
    Agora nesse exemplo o código está mais robusto, eu tenho mais opções, eu tenho mais condições,
eu tenho um 'if' perguntando se o carro é igual ao jetta
eu tenho um 'elif' para saber saber qual outros tipos de carros o usuario possa ter para retornar outro valor pra ele
e tambem tenho mais um 'else' para mostra outra mensagem para o usuario

é uma Estrutura condicional aninhada

'''