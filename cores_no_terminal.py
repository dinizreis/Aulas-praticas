'''
   Padrão ANSI --> é um padrão de normalização internacaional.
e ele tem o que a gente chama de ' escape sequence ' 

    eu vou usars esse escape sequence para o terminal do python.
tudo dentro do ANSI começa com 'contrabarra \ ' e um código.

obs: O código que funciona melhor para o python é o 033

sabendo disso, sempre que eu queiser reprensentar uma cor no terminal do python eu vou começar com o...
\033[ m .... e entre o [ e o m eu vou colocar o código.

segue o exemplo abaixo:

\033[style:text:backm  ou seja, no lugar de 'style' eu tenho que informar o estilo do texto, se ele é negrito, itálico ou sublinhado etc..
                        no lugar do 'texto' eu tenho que colocar qual é a cor do texto.
                        e 'back' eu tenho que colocar a cor do fundo de texto. esse é o esqueleto do meu codigo.

agora um exemplo real de um codigo: \033[0:33:44m


eis aqui uma tabela:

style               text                back
0 -> none            30 -> BRANCO        40 -> BRANCO
1 -> bold            31 -> VERMELHO      41 -> VERMELHO
4 -> sublinhado      32 -> VERDE         42 -> VERDE
7 -> negative        33 -> AMARELO       43 -> AMARELO
                     34 -> AZUL          44 -> AZUL
                     35 -> ROXO          45 -> ROXO
                     36 -> cyan          46 -> CYAN
                     37 -> cinza         47 -> CINZA


podemos fazer alguns testes qui:

teste com letra branca e fundo vermelho --> \033[0:30:41m
teste com letra amarelha e fundo azul  --> \033[4:33:44m
teste com letra roxa e fundo amarelo  --> \033[1:35:43m
teste com letra branca e fundo verde  --> \033[0:30:42m
teste com letra branca e fundo preto  --> \033[m
tesste com letra preta e fundo banco  --> \033[7:30m
 

AGORA ALGUNS EXEMPLOS:
'''

print("\033[7;30mHello, World!\033[m")