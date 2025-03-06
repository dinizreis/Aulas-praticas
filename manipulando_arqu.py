''' r = Leitura
    w = escrita e substitui o conteudo existente
    x = escrita, retorna um erro caso o arquivo ja exista ( é só para arquivos novos)
    a = escrita, insere novos dados mas ele na vai aterar nada no arquivo.
'''

# aqui vamos fazer um exemplo:

'''
aqui nesse comando open() eh para abrir o arquivo, open("empregados.txt", "w") dentro dos parenteses esta os parametros e
dentro das aspas esta o nome do aquivo que quero manipular e dentro da outra aspas está a letra que vai me permitir manipular o arquivo.
e eu posso atribuir tudo isso dentro de uma variavel.

'''
# empregados_file = open("empregados.txt", "a")
# empregados_file.write("Higor \nRenata \n")  # perceba que agora eu uso o nome da minha variavel que foi atribuida o aquivo. e agora com esse comando eu posso inserir qualqer coisa no meu arquivo.
# empregados_file.write("Rubia \nLeicia \n")    nomes que foram inseridos
# empregados_file.close()     # esse comando eh para feixar o arquivo

#____________________________________________________________________________________________________

'''
ultilizando listas junto com o comando open()
'''

def arquvivo_escreve():
    empregados_file = open("empregados.txt0","a")
    linhas = list() # esse eh o nome da minha lista.
    linhas.append("teste linha 1 \n")  # esse comando append() eh para adicionar itens a minha lista
    linhas.append("teste linha 2 \n")
    empregados_file.writelines(linhas) # comando usado para mander ele escrever nas linhas e dentro dos parenteses esta a minha variavel linha que eh a minha lista onde eu quero que ele escreva.
    empregados_file.close()

def leitura_arquivo():
    empregados_file = open("empregados.txt0", "r")
    for linha in empregados_file.readlines():
        print(linha)
    empregados_file.close()

arquvivo_escreve()
leitura_arquivo()