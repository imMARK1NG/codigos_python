tamanho = int(input("Digite o tamanho do vetor:"))
vetor = [int] * tamanho

for i in range(len(vetor)):
    vetor[i] = int(input(f"Digite o {i + 1} valor:"))

maior_valor = vetor[0]
menor_valor = vetor[0]

for i in range(len(vetor)):
    if vetor[i] > maior_valor:
        maior_valor = vetor[i]
    if vetor[i] < menor_valor:
        menor_valor = vetor[i]

print("Dados do vetor:\n")
for i in range(len(vetor)):
    print(vetor[i], end=" ")

print("\n")

print(f"O maior valor do vetor é {maior_valor}\n")
print(f"O menor valor do vetor é {menor_valor}")