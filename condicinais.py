n1 = float(input("Digite uma nota: "))
n2 = float(input("Digite a outra nota: "))
m = (n1 + n2)/2

print(f'A sua media foi {m:.1f}')

if m >= 7.00:
    print("Aprovado")
else:
    print("REPROVADO")
