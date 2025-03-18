#Dado um texto, contar quantas vezes cada palavra única aparece nele.

texto = input("insira um texto: ")
lista = texto.split(" ")
lista2 = []

for palavras in lista:
    lista2.append(palavras + ": " + str(lista.count(palavras)))

print(set(lista2))