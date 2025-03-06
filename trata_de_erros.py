# TRATAMENTO DE ERROS E EXECOES

# eh como se fosse uma condicional para tratamento de erro e execoes

numero = int(input("Digite um numero: "))
print(numero)

'''
    O que vai acontecer com esse codigo acima é que se o usuario digira um numero qualquer o codigo vai funciar bem, mas desde que seja 
apenas numeros, no entanto, se o usuario digitar alguma letra no lugar do numero o programa vai apresentar um erro.
e nesse caso, devemos colocar esse codigo dentro no TRY EXECEPT da forma que vamos fazer no exemplo abaixo.
'''

try:
    numero = int(input("Digite um numero: "))
    print(numero)
except:
    print("Caractere invalido!!")

'''
    O que acontece de diferente nessa estrutura de codigos é que se o usuario de faro digitar um numero no comando input
o comando print vai me mostra o numero que ele digitou e vai funcionar muito bem e o codigo só vai percorrer o try, mas se o usuario
digitar um texto no lugar do numero aí vai cair na condiçao do execept: print dizendo que o caractere é invalido. e assim o programa nao vai
parar de forma abrupita, irá apenas imprimir na tela que o erro que colocamos na condicao execept.

    Essa é a forma mais simples de usar o TRY - EXECEPT e é a menos recomendada. vamos dar outro exemplo abaixo de como seria uma das melhores
formas de se trabalhar com o TRY - EXECEPT.

'''

try:
    a = 10/0
    numero = int(input("Digite um numero: "))
    print(numero)
except ZeroDivisionError as erro:
    print(erro)
    print("Caractere invalido!!")


'''
    Entenda que o codigo esta dirente.
sabemos que nao da para fazer divisao por 0 (zero). mas coloquei esse exemplo apenas pra ele me mostrar o que de fato está errado no codigo
o que vamos fazer aqui é, fazer o TRY - EXECPET me mostrar a onde está o erro, qual é a linha de codigo errada.

    O exect ele deve ser tratato de forma a mostrar o nosso erro, e por isso ultilizamos o 'ZeroDivisionError as erro'  
com isso, ele vai imprimir o nosso erro. O nome 'erro' que está dentro de except é uma variavel e logo abaixo 
colocamos um print com essea variavel erro.

    E podemos também fazer mais de um except exatamente como mostra no ultimo exemplo de codigo.
'''

try:
    numero = int(input("Digite um numero: "))
    print(numero)
except ZeroDivisionError as erro:
    print(erro)
except:
    print("Caractere invalido!!")