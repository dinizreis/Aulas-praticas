# ESTUDO BASICO DE FUNCAO EXPONENCIAL

# VAMOS CRIAR UMA FUCAO PARA CHAMAR O NOSSO CALCULO DA FUNCAO EXPONENCIAL.

def calc_exponencial(num_base, num_expo):   # lembrando que o que vai dentro dos parenteses sao os argumentos/parametros da minha funcao
    resltado = 1
    for index in range(num_expo):
        resltado = resltado * num_base
    return resltado

print(calc_exponencial(3, 5))   