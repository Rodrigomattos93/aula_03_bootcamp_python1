#Simular tentativas de reconexão a um serviço com um limite máximo de tentativas

tentativas_maximas = 5
tentativa = 1

while tentativa <= tentativas_maximas:
    print(f"Tentativa número {tentativa}")
    tentativa = tentativa + 1
print("Número máximo de tentativas atingido.")