


INSUMOS_POR_MARMITA = {
    "arroz": 100,
    "feijao": 50,
    "carne": 25,
    "salada": 10
}


def calcular_marmitas_possiveis(estoque):
    return min(estoque["arroz"] // INSUMOS_POR_MARMITA["arroz"],
               estoque["feijao"] // INSUMOS_POR_MARMITA["feijao"],
               estoque["carne"] // INSUMOS_POR_MARMITA["carne"],
               estoque["salada"] // INSUMOS_POR_MARMITA["salada"])


estoque = {
    "arroz": float(input("Digite a quantidade de arroz no estoque (em gramas): ")),
    "feijao": float(input("Digite a quantidade de feijão no estoque (em gramas): ")),
    "carne": float(input("Digite a quantidade de carne no estoque (em gramas): ")),
    "salada": float(input("Digite a quantidade de salada no estoque (em gramas): "))
}

print("\nEstoque inicial:")
for item, qtd in estoque.items():
    print(f"{item.capitalize()}: {qtd} g")

print(f"\nCom esse estoque é possível fazer {calcular_marmitas_possiveis(estoque)} marmitas.\n")


while True:
    vender = input("Deseja vender uma marmita? (s/n): ").strip().lower()
    
    if vender == "n":
        print("Encerrando o sistema. Até logo!")
        break
    
    marmitas_possiveis = calcular_marmitas_possiveis(estoque)
    if marmitas_possiveis <= 0:
        print("⚠️ Estoque insuficiente para fazer mais marmitas!")
        break
    
  
    for item in estoque:
        estoque[item] -= INSUMOS_POR_MARMITA[item]
    
    print("\n✅ Marmita feita com sucesso!")
    print("Estoque atualizado:")
    for item, qtd in estoque.items():
        print(f"{item.capitalize()}: {qtd:.2f} g")
    
    print(f"\nAinda é possível fazer {calcular_marmitas_possiveis(estoque)} marmitas.\n")
