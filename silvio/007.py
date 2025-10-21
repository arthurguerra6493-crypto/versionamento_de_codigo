for _ in range(3):
    # Solicita ao usuário para digitar o nome da cidade
    nome_cidade = input("Digite o nome de uma cidade: ")
    # Adiciona o nome da cidade à lista
    cidades.append(nome_cidade)
    # Imprime a lista atualizada a cada iteração
    print(f"Lista atualizada: {cidades}")

# Imprime a lista final após o término do loop
print(f"\nLista final de cidades: {cidades}")