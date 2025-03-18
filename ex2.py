#Imagine que você está trabalhando com dados de sensores IoT. Os dados incluem medições de temperatura. Você precisa classificar cada leitura como 'Baixa', 'Normal' ou 'Alta'. Considerando que:
#Temperatura < 18°C é 'Baixa'
#Temperatura >= 18°C e <= 26°C é 'Normal'
#Temperatura > 26°C é 'Alta'

try:
    temperatura = float(input("Insira uma temperatura em ºC: "))

    if temperatura < 18:
        resultado = "baixa"
    elif temperatura >= 18 and temperatura <= 26:
        resultado = "normal"
    elif temperatura > 26:
        resultado = "alta"
    
    print(f"A temperatura é {resultado}!")

except ValueError as e:
    print(e)