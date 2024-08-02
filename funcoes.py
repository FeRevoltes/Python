#Função sem parãmetro
def saudacao():
    print("bom dia")

saudacao()

#Função com parâmetros
def saudacao(nome, curso):
    print(f"Seja bem-vinda(o), {nome}!")
    print(f"Começando o curso de {curso}")

saudacao("Fernando", "Python")

#função com parâmetro default
def saudacao(nome, curso="Python"):
    print(f"Seja bem-vinda(o), {nome}!")
    print(f"Começando o curso de {curso}")

saudacao("Fernando", "Javascript")

#Função com retorno
def soma(num1, num2):
    return num1 + num2

resultado = soma(5, 7)
print("Resultado: ", resultado)

def calculadora(num1, num2, op="+"):
    if op == "+":
        return num1 + num2
    elif op == "-":
        return num1 - num2
    elif op == "*":
        return num1 * num2
    elif op == "/":
        return num1 / num2
    else:
        print("Valor invalido!")

resultado = calculadora(5, 25, "*")
print("Resultado: ", resultado)
    