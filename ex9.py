#Dada uma lista de números, extrair apenas aqueles que são pares.

numeros = range(1,11)
lista = []
for i in numeros:
    if i % 2 == 0:
        lista.append(i)
print(lista)