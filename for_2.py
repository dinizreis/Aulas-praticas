'''
    Aula Gustavo Guanabara  --> LAÇO FOR OU ESTRUTURA DE REPETIÇÃO COM VARIAVEL DE CONTROLE

exemplo:

se fosse ler o comando for index in range() em portugues, seria mais ou menos assim:

    laco c no intervalo(0,3)
        passo
        pula        <-- ele vai percorrer esse comando tres vezez, porque dentro dos parenteses esta 0 , 3 ou seja, de 0 ate 3
    passo
    pega        <-- aqui eh o fim do comando.

agora, lendo esse mesmo comando na linguagem PYTHON

    for c in range(0,3):
        passo
        pula    <-- ele vai percorrer esse comando tres vezez, porque dentro dos parenteses esta 0 , 3 ou seja, de 0 ate 3
    passo
    pega    <-- aqui eh o fim do comando.
        
    
exemplos ...

'''
# for c in range(0, 7):
#     print(c)
# print("haha!")

#_________________________________

for a in range(0, 7, 2):   # aqui dentro dos parenteses é o parametro que eu quero, onde vai de 0 até 7
                        # agora, com mais uma virgula e o número 2 por exemplo, eu estou dizendo pra ele contar de 0 até 7 só que 
                        # pulando de dois em dois números.
    print(a)

#__________________________________________________________________

'''
    Vamos a um exemplo onde pedimos um numero para o usuario.
'''

n = int(input("Digite um numero inteiro: "))

for num in range(0, n):
    print(num)
print("FIM!")

#_________________________________________________________

i = int(input("Inicio: "))
f = int(input("Fim: "))
p = int(input("passo: "))

for c in range(i, f+1, p):
    print(c)
print("FIM!")

#_________________________________________________________

for b in range(0, 5):
    numero = int(input("Digite um numero: "))
print("FIM!")

'''
     Aqui nesse codigo, eu ultilizei a estrutura for e dentro dele eu pedi para o usuario digitar um numero
e o interessante eh que vai acontecer que o programa vai pedir para o usuario digitar o numero quantidade de vezes eu coloquei
na estruta for, que no caso foi de 0 ate 5 vezes.

    agora usando esse mesmo codigo, mas vamos somar os numeos que o usario digitar
'''
soma = 0    # para fazer esse tipo de soma a variavel tem que comecar valendo 0
for b in range(0, 4):
    num = int(input("Digite um numero: ")) 
    soma = soma + num
print(f"A Soma dos numeros eh {soma}")