numero_de_elementos = int(input("Digite o numero de elementos:"))
vetor = [i + 1 for i in range(numero_de_elementos)]
soma = 0

for i in range(len(vetor)):
    soma += i + 1

print(vetor)
print(soma)