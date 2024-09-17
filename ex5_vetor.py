tamanho = int(input("Digite o tamanho do vetor:")) #atribui um valor n para a variavel tamanho.
vetor = [int] * tamanho #declarando um vetor de numeros inteiros, * tamanho multiplica a quantidade de valores que teram dentro do vetor.

for i in range(len(vetor)): #laço para percorrer o vetor.
    vetor[i] = int(input(f"Digite o {i + 1} valor:")) #atribui valores n valores inteiros no vetor.

maior_valor = vetor[0] #atribuindo a posição zero do vetor a variavel maior_valor.
menor_valor = vetor[0] #atribuindo a posição zero do vetor a variavel menor_valor.

for i in range(len(vetor)): #laço pra percorrer o vetor.
    if vetor[i] > maior_valor: #condição para saber se o valor do vetor é maior que o valor q tá na variavel maior_valor.
        maior_valor = vetor[i] #caso seja verdade a variavel maior_valor recebe o valor do vetor[i].
    if vetor[i] < menor_valor: #condição para saber se o valor do vetor é menor que o valor q tá na variavel menor_valor.
        menor_valor = vetor[i] #caso seja verdade a variavel menor_valor recebe o valor do vetor[i].

print("Dados do vetor:\n") #imprime os dados que estão entre aspas na tela.
for i in range(len(vetor)): #laço pra pecorrer o vetor.
    print(vetor[i], end=" ") #imprime o dados que estão guardados dentro do vetor[i] na tela;

print("\n") #quebra de linha

print(f"O maior valor do vetor é {maior_valor}\n") #imprime os dados que estão entre aspas e os dados da variavel maior_valor na tela.
print(f"O menor valor do vetor é {menor_valor}") #imprime os dados que estão entre aspas e os dados da variavel menor_valor na tela.