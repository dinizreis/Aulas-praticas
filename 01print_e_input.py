# nome = "Higor"
# idade = "30"
# gosto_de = "estudar"

# print(f"Olá! meu nome é {nome}!")
# print(f"Eu tenho {idade} anos de idade")
# print(f"e eu gosto muito de {gosto_de}")
# print(f"Bom, o {nome} disse que tem {idade} anos de idade e que gosta muito de {gosto_de}")

#-----------------------------------------------------------------------------------------------

# nome = input("Digite seu nome: ")

# print(f"seja bem-vindo(a), {nome}!")

#----------------------------------------------

# nome = input("Dige seu nome: ")

# print(f"Ola, {nome} seja bem-vindo(a)!")
# print(f"{nome}, preciso de algumas informacoes sua!")

# dia = input("Digite o dia do seu nascimento: ")
# mes = input("Digite o mes do seu nascmento: ")
# ano = input("Digite o ano do seu nascimento: ")

# print(f"muito bem, sabemos entao que voce nasceu no {dia}/{mes}/{ano} ")

#------------------------------------------------------------------------------

# num1 = int(input("digite um numero para ser resolvido: ") )
# num2 = int(input("digite outro numero: "))

# resultado = num1 + num2

# print(f"A soma entre {num1} e {num2} e de: {resultado} ")

#--------------------------------------------------------------------

print("Ola, World!")
print("Vamos comecar!")

nome = input("DIgite o seu nome: ")
print(f"Seja bem-Vindo(a) {nome}!")

cidade = input(" de onde voce veio? qual e a sua cidade? ")
print(f"Voce veio de muito longe {nome}, {cidade} e muito longe.")

print("E necessario saber sua idade")
idade = input("Digite a sua idade: ")

print(f"Bom {nome}, voce acha que com {idade} anos voce sera capaz de fazer o trabalho?")

estoupronto = input(" voce acha que estar pronto? digite s para sim e n para nao: ")

if estoupronto == "s":
    print("e capaz!")
else:
    print("nao e capaz")

print("Bom, entendo que seja capaz! \n agora, perciso que resolsa uma pequena questao pra mim.\n Resolva para mim a seguinte conta")
print("50*6+7")

resultado1 = int(input("qual e o resultado da questao? "))

if int(resultado1 == 307):
    print("Resposta correta")
else:
    print("Resposta incorreta!")



#___________________________________________________________________
# n = input("Digite algo: ")
# print(n.isalnum())

#____________________________________________________________________

'''
    Curiosidados do prints()

''' 

nome = input("Digite seu nome: ")
print("Prazer em te conhecer {:20}!".format(nome))  
# usando o printe dessa maneira colocaando dentro das chaves o {:20} e dentro do .formate(nome) você tera o seguinte resultado... 
# (aperte para rodar o programa)

nome = input("Digite seu nome: ")
print("Prazer em te conhecer {:=>20}!".format(nome))
# usando o printe dessa maneira colando dentro das chaves o {:=>20} e dentro do .formate(nome) voce tera o seguinte resultado... 
# (aperte para rodar o programa)

nome = input("Digite seu nome: ")
print("Prazer em te conhecer {:=<20}!".format(nome))
# usando o printe dessa maneira colando dentro das chaves o {:=<20} e dentro do .formate(nome) voce tera o seguinte resultado... 
# (aperte para rodar o programa)

nome = input("Digite seu nome: ")
print("Prazer em te conhecer {:^20}!".format(nome))
# usando o printe dessa maneira colando dentro das chaves o {:^20} e dentro do .formate(nome) voce tera o seguinte resultado... 
# (aperte para rodar o programa)

nome = input("Digite seu nome: ")
print("Prazer em te conhecer {:=^20}!".format(nome))
# usando o printe dessa maneira colando dentro das chaves o {:=^20} e dentro do .formate(nome) voce tera o seguinte resultado... 
# (aperte para rodar o programa)

nome = input("Digite seu nome: ")
print("Prazer em te conhecer {:=^20}!".format(nome))