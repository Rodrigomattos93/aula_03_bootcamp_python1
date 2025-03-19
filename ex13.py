#Simular o consumo de uma API paginada, onde cada "página" de dados é processada em loop até que não haja mais páginas.

pagina_atual = 1
paginas_totais = 5  # Simulação, na prática, isso viria da API

while pagina_atual in range (1, paginas_totais+1):
    print(f"Página {pagina_atual} processada")
    pagina_atual = pagina_atual + 1
    
print("Fim. Todas as páginas foram processadas")
