idade = 20
if idade > 18:
    print("Maior de idade")
else:
    print("Menor de idade")

#Condicional composta
nota1 = 8
nota2 = 3
nota3 = 10
nota4 = 9
media = (nota1 + nota2 + nota3 + nota4) / 4
presensa = 100

if media >= 7 and presensa >= 70:
    print("Aprovado!", media)
    print("Parabéns")
elif media >= 5 and presensa >= 70:
    print("Recuperação", media)
else:
    print("Reprovado!", media)