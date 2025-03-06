# abacaxi

# a - d
# b - e
# c - f
# x - a
# i - l

# dedfdal

alfabeto = ["a", "b","c","d","e","f","g","h","i","j","k","l","m","n","o","p","q","r","s","t","u","v","x","y","z"]

chave = 3
mensagem = "abacaxi"
mensagem = mensagem.lower()

# Tamanho da lista alfabeto
n = 128    #n = len(alfabeto)
cifrada = ""

for letra in mensagem:  # Para cada letra da mensagem:
    #ord()
    #chr()
    #achar no alfabeto a letra que esteja chave posisoes a frente na tabela ASCII

    indice = ord(letra)    #indice = alfabeto.index(letra)   
    nova_letra = chr((indice + chave)%n)     #nova_letra = alfabeto[(indice + chave)%n]
    cifrada = cifrada + nova_letra  # substituir na mensagem a letra pela nova_letra


# exibi mensagem cifrada

print(mensagem)
print(cifrada)