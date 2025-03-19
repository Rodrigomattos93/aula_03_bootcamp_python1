#Processar itens de uma lista até encontrar um valor específico que indica a parada.

itens = [1, 2, 3, "parar", 4, 5]

i = 0
while i < len(itens):
    print(itens[i])
    if itens[i] == "parar":
        break
    i = i +1