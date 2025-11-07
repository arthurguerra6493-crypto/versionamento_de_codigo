numeros = [10,7,5,8,9,0,]
numero_usuario = int(input("Digite um número para verificar se está na lista: "))
num = [0.1,0.0,0.3,1.3]
numero_pessoal = float(input("Digite um número decimal para verificar se está na lista: "))
if numero_pessoal in num:
    print(f"o numero {numero_usuario} foi encontrado")
else:
    print(f"o numero {numero_usuario} não foi encontrado")
if numero_usuario in numeros:
    print(f"o numero {numero_pessoal} foi encontrado")
else:
    print(f"o numero {numero_pessoal} não foi encontrado")

 
