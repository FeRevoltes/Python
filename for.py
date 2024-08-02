for i in  range(10):
    print(i)

for i in range(1, 15, 3):
    print(i)


soma = 0
for i in range(1, 4):
    nota = float(input(f"Informe nota {i}: "))
    soma = soma + nota
print("Media:", soma / 3) 