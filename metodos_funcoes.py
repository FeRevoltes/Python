# Método de lista
lista = [1, 3, 12, 8, 2]

#append
print(lista)
lista.append(4)
print(lista)

#insert
lista.insert(2, 44)
print(lista)

#extend
lista2 = [2, 5, 7]
lista.extend(lista2)
print(lista)

#pop
lista.pop()
lista.pop(1)
print(lista)

#remove
lista.remove(8)
print(lista)

#count
print(lista.count(2))

#index
print(lista.index(4))

#sort
lista.sort()
print(lista)
lista.sort(reverse=True)
print(lista)

#funções para listas

#len
print(len(lista))

#sum
print(sum(lista))

#max e min
print(max(lista))
print(min(lista))