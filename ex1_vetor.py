vetor = [1,2,4,16,32,64,-128] #definindo um vetor com 10 elementos.

maior_n = vetor[0] #atribuindo a posição zero do vetor a variavel maior_n.
menor_n = vetor[0] #atribuindo a posição zero do vetor a variavel menor_n.


for i in range(len(vetor)): #laço pra percorrer o vetor.
    if vetor[i] > maior_n: #condição para saber se o valor do vetor é maior que o valor q tá na variavel maior_n.
        maior_n = vetor[i] #caso seja verdade a variavel maior_n recebe o valor do vetor[i].
    elif vetor[i] < menor_n: #condição para saber se o valor do vetor é menor que o valor q tá na variavel menor_n.
        menor_n = vetor[i] #caso seja verdade a variavel maior_n recebe o valor do vetor[i].



print("Dados do vetor") #imprime os dados que estão entre aspas na tela.
for i in range(len(vetor)): #laço pra pecorrer o vetor.
    print(vetor[i]) #imprime o dados que estão guardados dentro do vetor[i] na tela;

print("o maior valor é:", maior_n) #imprime os dados que estão entre aspas e os dados da variavel maior_n na tela.

print("o menor valor é:", menor_n) #imprime os dados que estão entre aspas e os dados da variavel menor_n na tela.
