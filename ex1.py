#Você está analisando um conjunto de dados de vendas e precisa garantir que todos os registros tenham valores positivos para quantidade e preço. Escreva um programa que verifique esses campos e imprima "Dados válidos" se ambos forem positivos ou "Dados inválidos" caso contrário.

try:
    qtd = int(input("indique a quantidade: "))
    preco = float(input("indique o preço: "))


    if qtd <=0 or preco <= 0:
        print("dados inválidos")
    else:
        print("dados válidos")

except ValueError as e:
    print(e)
