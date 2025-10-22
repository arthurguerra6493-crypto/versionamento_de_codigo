lista_cidades = ["belo horizonte"]

print(f"lista inicial: {lista_cidades}")

for i in range(3):
    nova_cidade = input (f"digite o nome da {i+i} a cidade: ")
    lista_cidades.append(nova_cidade)
    print(f"lista atualizada: {lista_cidades}")