# import manipulando_arqu

# manipulando_arqu.arquvivo_escreve()

#________________________________________________________________

'''
    Aqui vou usar um exemplo importano um módulo de matemática ( math ) 
veja no exemplo abaixo ultilizando da forma 'Import'

'''

# import math     # aqui eh usado para importar qualquer modeulo e nesse caso foi modulo 'math'

# num = int(input("DIgite um número: "))  # aqui eu criei uma variavel chamada 'num' que vai receber o numero inteiro vindo do usuario.
# raiz = math.sqrt(num)       # aqui uma variavel 'raiz' usando o modulo importado 'math' e com a funcao 'sqrt' que significar raiz quadrada, e entre os parenteses esta a variavel num
# print(f"A raiz quadrada de {num} é {math.floor(raiz)}")     # aqui eh vai imprimir na tela o numero do usuario mais a rais quadrada desse mesmo numero.8

#____________________________________________________________________

''' 
    aqui vamos trabalhar também com imprtacao mas de uma forma um pouo diferente, vou importar o modulo matematica só que dessa vez
eu quero importa apenas algumas funcionalidades do modulo.

a diferenca do modo de importar ' Impor math ' para o 'from math import' é que no import math eu importo todos os recursos que o modulo tem.
e no modo 'from math impor ' que escrevo logo na frente a funcionalidade que eu preciso e seu eu precisar mais de uma funcionalidade eu 
coloco virgula (,) e a outra funcionalidade.

'''
import math

n1 = float(input("Digite um número: "))
raiz = math.sqrt(n1)

print(f"A Raiz quadrada de {n1} é {math.floor29(raiz)}")

#_______________________________________________________________

from math import sqrt

n2 = float(input("Digite um número: "))
raiz = sqrt(n2)

print(f"A raiz quadrada de {n2:.0f} é {raiz:.2f}")

#_______________________________________________________________

'''
    modulo para gerar numeros aleatorios import random

'''

import random

n3 = random.random()
print(n3)

'''
    ramdint() pode me dar um numero qualqer desde que entre parenteses eu colo de qual a qual numero ele vai gera aleatoriamente.. 
por exemplo.

'''
import random

n4 = random.randint(1, 20)
print(n4)

#___________________________________________________________

'''
    Aqui eu baixei um modulo da internet chamada emoji, para usar os amojis que eu precisar
basta seguir o exemplo que abaixo.

'''

import emoji
print(emoji.emojize("python is :thumbs_up:"))
print(emoji.emojize("Renata é meu amor :red_heart:"))
print(emoji.emojize("Hello, World :globe_showing_Americas:"))