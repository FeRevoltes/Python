#Criando dicionário

dicionario = {}
dicionario = dict()

dicionario = { "Nome": "Walisson", "idade": 26, "altura": 1.77}
print(dicionario)
print(dicionario['idade'])

dicionario["programador"] = True
print(dicionario)

dicionario["altura"] = 2
print(dicionario)

#Iterando sobre um dicionário
for i in dicionario:
    print(i, dicionario[i])

#Testando a existência de chave
print("peso" in dicionario)
print("altura" in dicionario)