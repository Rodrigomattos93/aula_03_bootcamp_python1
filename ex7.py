#Normalizar uma lista de números para que fiquem na escala de 0 a 1.

lista = input("Insira uma lista separada por vírgulas: ")
lista = lista.split(",")
lista2 = []

for i in lista:
    lista2.append(int(i))

lista2_max = max(lista2)
lista2_min = min(lista2)

lista3 = []

for j in lista2:
    k = (j - lista2_min) / (lista2_max - lista2_min)
    lista3.append(k)

print(lista3)