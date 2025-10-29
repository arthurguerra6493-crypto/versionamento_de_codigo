lista_frutas = []


frutas_a_digitar = ["Laranja", "Banana", "Limão", "Pera", "Uva"]


print("Por favor, digite as seguintes frutas na ordem:")
for fruta in frutas_a_digitar:
    entrada_usuario = input(f"Digite '{fruta}': ")
   
    if entrada_usuario.strip().capitalize() == fruta:
        lista_frutas.append(entrada_usuario.strip().capitalize())
        print(f"'{entrada_usuario.strip().capitalize()}' adicionada.")
    else:
        print(f"Entrada inválida. A fruta esperada era '{fruta}'. A lista será criada com a fruta correta.")
        lista_frutas.append(fruta)


print("\nLista de frutas final:")
print(lista_frutas)
