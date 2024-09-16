tamanho = int(input("Digite o tamanho do  vetor:"))
vetor = [int] * tamanho
soma = 0
for i in range(len(vetor)):
    vetor[i] = int(input(f"Digite o {i + 1} valor:"))

print("\n")

print("Dados do vetor:")
for i in range(len(vetor)):
    print(vetor[i], end=" ")

print("\n")

pos1 = int(input("Digite a primeira posição:"))
pos2 = int(input("Digite a segunda posição:"))

x = vetor[pos1]
y = vetor[pos2]

soma = x + y

print("primeiro numero selecionado:",x)
print("segundo numero selecionado:",y)
print("a soma é igual a:",soma)

