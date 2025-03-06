'''
                                                OPERADORES ARITIMÉTICOS

 -> OS PRINCIPAIS OPERADORES ARITIMETICOS:

 + (soma)
  - (Subtracao) 
 * (Multiplicacao) 
 / (divisao)  
 // (divisao com arredondamento)
  % (resto) 
 ** (esponenciacao) 

                                                'ORDEM DE PRECEDENCIA'

    Significa qual ou quem vai ser o primeiro a ser calculado numa exressao matemática.

1 -> () : quem tivre entre os parenteses será calculado primeiro. depois de resolver os que estao dentro dos parenteses sao os...
2 ->  ** : as ** (potencias) ou seja, as exponenciação é a segunda ordem de precedenia a ser resolvida e/ou a segunda coisa mais importante dentro de uma aritimética.
3 -> ( * , / , // , % ) a tercia coisa é a  * multilicacao, / divisao, // divisão inteira e % resto da divisao.
OBS: se dentro de uma expressao conter todas essas experessoes * / // % , ai temos que resovler o que vinhé primeiro, 
mas seguindo a ordem primerio os () parenteses depois as exponensiacao ** e depois o que vinhé primeiro dos * / // %   
e por ultimo vamos resolver os...
4 -> + , - : resolver as somas e as subtacao binárias, ou seja, somar ou subtrair dois numeros.

exemplos:

    5 + 3 * 2 == 11
(Peimeiro vamos resolver 3*2 que vai dar 6 e depois vamos somar 6 + 5 que vai dar 11)

    3 * 5 + 4 ** 2 == 31
(Primeiro vamos resolver 4 ** 2 (exponenciacao 4 * 4) que vai dar 16 e depois vamos multiplicar 3 * 5 que vai dar 15
e depois vamos somar 16 + 15 e vamos ter o resultado de 31)

    o mesmo exemplo de cima, só que um pouco diferente!
    3 * (5+4) ** 2 == 243
(nesse exemplo ja temos o 5+4 dentro dos parenteses ou seja, eles serao resolvios primeiro. entao, 5+4 vai dar 9 
depois vamos fazer 9**2 (que nada mais é que 9*9 'exponenciacao') que vai dar 81 e depois vamos multiplicar 81 * 3 e vai dar 243 )

'''
'''
                                                    OPERADORES LOGICOS 

 And
 Or
 Not

                                                    OPERADORES RELACIONAIS

 == IGUAL
 !=  diferente
 > maior
 < menor
 >= maior igual
 < menor igual

'''


'''
                                                    OPERADORES DE ATRIBU8ICAO

 = 
 += 

'''
#____________________________________________________________________________________________________

n1 = int(input("Digite um numero: "))
n2 = int(input("Digite outro numero: "))

print(f"A soma de {n1} + {n2} e:", n1+n2)

#________________________________

n3 = int(input("Digite o n3: "))
n4 = int(input("DIgite o n4: "))
s = n3 + n4
m = n3 * n4
d = n3 / n4
di = n3 // n4
e = n3 ** n4

print(f"A soma de {n3} + {n4} é: {s} \n A multiplicacao de {n3} * {n4} é: {m} \n A divisao de {n3} / {n4} é: {d}\n A divisao inteira de {n3} // {n4} é: {di} \n A Exponeciacao de {n3} ** {n3} é: {e}")

#___________________________________________

