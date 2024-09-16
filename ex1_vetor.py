tamanho = int(input("Digite o tamanho:"))
vetor = [int] * tamanho


for i in range(len(vetor)):
    vetor[i] = int(input(f"Digite o {i + 1} valor:"))

maior_n = vetor[0]
menor_n = vetor[0]


for i in range(len(vetor)):
    if vetor[i] > maior_n:
        maior_n = vetor[i]
    else:
        menor_n = vetor[i]



print("Dados do vetor")
for i in range(len(vetor)):
    print(vetor[i])

print("o maior valor é:", maior_n)

print("o menor valor é:", menor_n)
