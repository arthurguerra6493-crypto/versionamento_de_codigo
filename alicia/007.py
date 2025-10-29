cidades = []

while True:
  nome = input(" Digite o nome da cidade (ou digite 'sair' para encerrar):")
  if nome.lower() == 'sair':
       break 
  cidades.append (nome)
  print("lista atualizada de cidades:" , cidades)

print("\nPrograma encerrado.")
print("Lista final de cidades:",cidades)