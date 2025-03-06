                                                # MANIPULANDO TEXTO.

'''
     FATIAMENTO

    Fatiar uma string é conseguir pegar pedaços dela
Segue o exemplo abaixo!

'''

frase = "Curso em Video Python"
print(frase)
#______________
print(frase[9])
#_______________
print(frase[9:13])
#_________________
print(frase[9:21:2])
#____________________
print(frase[:5])
#_______________
print(frase[15:])
#_________________
print(frase[9::3])
'''
    O simbolo de colchetes [] quer dizer listas.
nesse exemplo, dei um print() com a variavel frase e, normalmente era para o comando printar na tela o que está contido na variavel frase.
no entanto o que vai mudar aqui com esses colchetes [] é que dentro deles há o numero 9 da seguinte maneira print(frase[9])
isso quer dizer que ele vai imprimir pra mim só a letra que há na cadeia de caractere 9 da minha frase, que no caso é a letra 'V' lembando que
a contagem começa sempre do zero ( 0 )

    Um outro exemplo --> print(frase[9:13]) <-- aqui nessa situação é um pouco diferente, ele está agora entre colchetes 9:13
isso quer dizer que ele vai comecar da posição 9 e vai contar até o 13 posição da minha cadeia de caractere contida na minha variavel frase.
SÓ QUE NA VERDADE, ELE VAI EXCLUIR O CARACTERE 13 E VAI CONTAR ATÉ O CARACTERE 12 no caso ele vai escrever na tela 'Vide'

    Aqui nesse outro exemplo --> print(frase[9:21:2]) <-- eu posso ver que ele está um pouco diferente, tem umas informações a mais ali
bom, a ideia continua sendo a mesma, entre os colchetes [9:21:2] isso quer dizer que ele vai comecar a contar do caractere da posição 9 
e vai até o último caracter só que ele vai pulando de 2 em 2 caractere, é isso que outro 2 quer dizer. ou seja, ele vai pular algumas letras.

    Aqui nesse outro exemplo --> print(frase[:5]) <-- está agora diferente, entre os [:5] eu tenho apenas :5 o que quer dizer que ele vai
comecar a contar do caractere 0 (zero) e vai até o caractere 5 mas lembrando que vai mostrar até o caractere 4.

    Aqui nesse outro exemplo --> print(frase[15:]) <-- é semelhando ao exemplo de cima, a diferença é que ele vai comecar do caraceter 15
e como nao tem nada depois dos ' : ' ele vai até o final da frase.
    
    aqui nesse outro exemplo --> print(frase[9::3]) <-- a idéia é uma pouco a mesma, repara que dentro dos colchetes [] eu tenho
[9::3] sendo que o 9 é novamente de onde ele vai comecar a contar dentro da frase, entre os :: não tem nenhum número, entao isso quer dizer que
ele vai contar até o final, e o numero 3 quer dizer que ele ai pulando de 3 em 3 caractere


'''

                                                    # ANALISE

'''
    ANALISAR UMA STRING É QUE MAIS VAMOS USAR, PARA POR EXEMPLO SABER O 'TAMANHO DELA' , 'COMO QUE LETRA ELA COMEÇA' , 'COM QUE LETRA ELA TERMINA'
são essas e outras coisas que vamos analisar.

'''

print(len(frase))
#_________________
print(frase.count("o"))
#_______________________
print(frase.count("o",0,13))
#___________________________
print(frase.find("deo"))
#___________________________
print(frase.find("Android"))
#____________________________
print("curso" in frase)


'''
    a primeira analise será com o 'len() e len vem de 'length' que quer dizer comprimento.
ou seja, com isso eu quero saber qual é o comprimento dessa cadeia de caractere da minha variavel.'

    Aqui nesse exemplo --> print(frase.count("o")) <-- frase.count() eu quero que ele conte alguma coisa, e nesse caso entre as aspas
eu quero que ele conte quantas letras "o" tem na minha cadeia de caractere da minha variavel frase.

    Aqui nesse exemplo -->  print(frase.count("o",0,13))  <-- entre os parenteses () esta entre as aspas a letra o que é o caractere
que eu quero que ele procure. depois tem o número ' 0 ' e isso porque estou dizendo para ele comecar a contar do caracter 0 e ir até o caractere
13. ou seja, de 0 a 13 ele vai contar quantas letras o eu tenho no caratere da minha variavel frase.

    Aqui nesse outro exemplo -->  print(frase.find("deo"))  <--- eu ultilizei o 'find' e find quer dizer encontrar, entao eu estou pedindo
para ele entrar os caracteres "deo", entao ele vai percorrer por todo o caractere da variavel frase e se encontrar ele vai me mostrar em qual
posição ele comeca.

    Aqui nesse outro exemplo --> print(frase.find("Android")) <-- se eu colocar dentro do find() um valor que nao existe ele vai me retorna -1

    Aqui nesse exemplo --> print("curso" in frase) <-- ele está pergurando se existe a palavra 'curso' dentro da variavel frase se tiver a palavra
'curso' ele vai retornar pra mim 'True' e se nao tiver a palavra ele vai retornar 'False'

'''

                                                # TRANSFORMAÇÃO

'''
    POr via de regra uma 'Lista' de string ela é imutável, ou seja, nao podemos mudar ela. MAS EU CONSIGO MUDAR ELA ATRAVÉS DOS METODOS

'''

print(frase.replace("Python","CSharp"))
#________________________________________
print(frase.upper())
#____________________
print(frase.lower())
#____________________
print(frase.capitalize())
#_________________________
print(frase.title())
#__________________
print(frase.strip())
#____________________
print(frase.rstrip())
#_____________________
print(frase.lstrip())

'''
    Aqui temos um exemplo --> print(frase.replace("Python","CSharp")) <-- aqui eu estou usando o .replace() para trocar.
a primeria palavra dentro da primeira aspas pela a palavra que está dentro da segunda aspas
no exemplo acima quero trocar a palavra python pela palavra Csharp

    Aqui nesse outro exemplo --> print(frase.upper()) <-- o .upper() vai colocar pra mim todas as letras em maiusculas.

    já o --> lower() <-- ele vai deixar as letras em minusculas.

    Aqui nesse outro exemplo --> print(frase.capitalize()) <-- ele vai jogar todos os caracteres para minusculas, isto é, ele vai jogar todas as
letras para minusculas e vai deixar só a primeira letra em maiuscula.

    aqui nesse exemplo --> print(frase.title()) <-- ele vai analisar quantas 'PALAVRAS' a minha string tem e vai transformar cada letra
de incio de palavra em maiuscula

    Esse exemplo é muito importante: --> print(frase.strip()) <-- porque ele remove todos os espacos desnecessários antes e depois do texto.

    DIferentemente da outra funcao o --> print(frase.rstrip()) <-- o rstrip() ele vai remover apenas os espacos desnecessario da direita o 'r'
vem de ' right ' ou seja, 'direta' 

    De forma parecida eu tenho o --> print(frase.lstrip()) o lstrip() ele vai remover apenas o espacos inuteis da esquerda o 'l' vem de 
' left ' que quer dizer 'esquerda'

'''

                                                    # DIVISÃO

print(frase.split())
#______________________
print("-".join(frase))

'''
    Aqui nesse primeiro exemplo eu tenho o --> print(frase.split()) <-- O .split() tem algumas funcionalidades a mais alem de deixar os parenteses ()
vazio OBS: vale uma estudada apenas do split()
MAS O .SPLIT() ELE TECNICAMENTE ELE GERA UMA LISTA COM TODAS AS PALAVRAS DE UMA CADEIA DE CARACTERERS, ELE VAI SEPARAR AS PALAVRAS E CADA
PALAVRA VAI TER UMA NUMERACAO DIFERENTE

    Outro exemplo muito útiu e importante é esse --> print("-".join(frase)) <-- ela funciona sa seguinte maneira, entre as aspas está um traco -
e logo em segida .join() e dentro dos parentes eu tenho a variavel frase ficando da seguinte maneia print("-".join(frase)) eu estou dizendo que 
as eu vou 'separar' a o texto contido na minha variavel frase com os ( - ) tracos 

'''