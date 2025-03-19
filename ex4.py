#Antes de processar os dados de usuários em um sistema de recomendação, você precisa garantir que cada usuário tenha idade entre 18 e 65 anos e tenha fornecido um email válido. Escreva um programa que valide essas condições e imprima "Dados de usuário válidos" ou o erro específico encontrado.

try:
    email = input("Insira seu e-mail: ")
    idade = int(input("Insira sua idade: "))
    posicao_arroba = email.rfind("@")

    if "@" not in email or "." not in email or email.count("@") > 1:
        print("Formato de e-mail inválido")
        exit()
    elif len(email[posicao_arroba+1:]) == 0 or len(email[:posicao_arroba]) == 0:
        print("Formato de e-mail inválido")
        exit()
    elif idade >= 18 and idade <= 65:
        print("Dados de usuário válidos")
    else:
        print("Idade deve estar entre 18 e 65 anos.")
except ValueError as e:
    print(e)