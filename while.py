import random
numR = random.randint(1, 10)

numE = int(input("Informe um número entre 1 e 10: "))

while numE != numR:
    print("Você errou, Tente novamente!")
    numE = int(input("Informe um número entre 1 e 10: "))

print("Parabéns, você acertou!")

#Exemplo 2
contador = 0

while contador <= 5:
    print(contador)
    contador += 1