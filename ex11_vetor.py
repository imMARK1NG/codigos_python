vetor =[int] * 6 #declarando um vetor com espaço pra 6 valores inteiros.

for i in range(len(vetor)): #laço pra pecorrer o vetor.
    vetor[i] = int(input(f"Digite o {i + 1} valor:")) #atribui os valores informados pelo usuario ao vetor.

vetor_inverso = vetor[::-1] #inverte os dados do vetor, slicing(fatiamento [::-1] inicio:fim: passo.)

print("\n") #quebra de linha.
print("Dados do vetor:",vetor) #imprime os dados da variavel vetor e mostra na tela.
print("Dados do vetor_inverso:",vetor_inverso) #imprime os dados da variavel vetor_inverso e mostra na tela.
