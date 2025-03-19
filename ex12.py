#Solicitar ao usuário um número dentro de um intervalo específico até que a entrada seja válida.

entrada = ""

while entrada not in range(1,11):
    try:
        entrada = int(input("digite um número entre 1 e 10: "))
    except ValueError as e:
        print(e)