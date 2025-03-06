# Laco de repeticao WHILE ou ESTRUTURA DE REPETIÇÃO COM TESTE LÓGICO.

'''
    Primeiro vamos fazer uma comparação do LAÇO DE REPETIÇÃO FOR 
e depois vamos fazer o LAÇO DE REPETIÇÃO WHILE. Apenas pra gente intender e percer as diferencas entre os dois
e saber quando usar um e quando usar o outro.

vamos ao laço for primeiro
'''

'''
--> aqui nesse laço for bem simples, sabemos que ele vai contar de 1 até o numero 10.
e ja sabemos que para ele contar até número 10 preciso colocar um número a mais.

o for eu uso quando eu sei o limite.
'''
for c in range(1, 11):
    print(c)
print("fim!")

'''
    Agora vou fazer essa mesma idéia com laço while
o while eu uso quando eu nao sei o limite.
'''

c = 1
while c < 10: # aqui ele está dizendo o seguinte: enquanto o c for menor que 10. lembrando que c recebe 1.
    print(c)
    c = c + 1
print("Acabou!")

# vamos a outros exemplos de laco WHILE

numero = 1
while numero != 0: # aqui eu ele esta dizendo o seguinte: enquanto o numero for diferente de 0, continue...
    numero = int(input("Digite um numero: "))
print("Fim!")

#______________________________________________________________________________________________

'''
    Eu quero que ele me diga quantos numeros digitados foram pares e quantos foram impares
'''

num = 1
par = impar = 0
while num != 0:
    num = int(input("Digite um valor: "))
    if num != 0:
        if num % 2 == 0:
            par = par + 1
        else:
            impar = impar + 1
print(f"Voce digitou {par} numeros e {impar} numeros!")