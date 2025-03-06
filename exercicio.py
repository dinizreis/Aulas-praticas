# Lista de Exercicios 

# Faça um programa que verifique se uma letra digitada é vogal ou consoante

# vogal = input("Digite uma letra: ")


# if vogal == "a" or  vogal == "e" or vogal == "i" or vogal == "o" or vogal == "u":
#     print("È uma vogal!")
# else:
#     print("é uma Consoante!")

    #_________________________________________________________________________________


nota1 = float(input("Qual foi a sua primeia nota? "))
nota2 = float(input("Qual foi a sua segunda nota? "))
nota3 = float(input("Qual foi a sua terceira nota? "))
nota4 = float(input("Qual foi a sua quarta nota? "))

media = (nota1 + nota2 + nota3 + nota4) / 4

print(f"Sua média é: {media}")

if media < 7:
    print("Reprovado!")
elif media > 7:
    print("APROVAdO!")
elif media == 10.0:
    print("Parabens!")
else:
    print("Aprovado com distincao!")