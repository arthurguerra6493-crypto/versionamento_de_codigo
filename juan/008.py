
cidades = []

print("Digite os nomes das cidades ou digite 'sair' para encerrar:")


while True:
   
    nome_cidade = input("Digite o nome da cidade: ")
    
   
    if nome_cidade.lower() == 'sair':
        print("Programa Encerrado..........")
        break
    else:
      
        cidades.append(nome_cidade)


print("\nLista de cidades :")
for cidade in cidades:
    print(f"- {cidade}")

