tamanho = 10 #atribuindo um valor para a variavel tamanho.
vetor_1 = [int] * tamanho #declarando um vetor de numeros inteiros, * tamanho multiplica a quantidade de valores que teram dentro do vetor.

quadrado = 0 #declarando a variavel quadrado e a inicializando com o valor zero.

for i in range(len(vetor_1)): #laço para percorrer o vetor.
    vetor_1[i] = int(input(f"Digite o {i + 1}° valor:")) #atribui valores inteiros no vetor, valores definidos pelo usuario.

print("Dados do vetor:\n",vetor_1, end=" ") #imprime os dados que estão dentro do vetor_1, end=" " coloca no final um espaço vazio.

print("\n") #quebra de linha.

quadrado = [vetor_1[i] ** 2 for i in range(len(vetor_1))] #vetor[i] ** 2 atribui a cada elemento o seu valor ao quadrado.


print(f"O quadrado dos elementos do vetor:\n {quadrado}") #imprime os dados que estão dentro da variavel quadrado.




