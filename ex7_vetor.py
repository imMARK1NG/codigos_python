tamanho = 5 #define o tamanho do vetor

#define a quantidade de numeros inteiros que o vetor vai ter.
vetor = [int] * tamanho
vetor_2 = [int] * tamanho
vetor_3 = [int] * tamanho

print("Dados do vetor:") #imprime os dados que estão entre aspas na tela.
for i in range(len(vetor)): #laço pra percorrer o vetor.
    vetor[i] = int(input(f"Digite o {i + 1} valor:"))#atribui n valores inteiros no vetor.

print("Dados do vetor_2:") #imprime os dados que estão entre aspas na tela.
for j in  range(len(vetor_2)): #laço pra percorrer o vetor.
    vetor_2[j] = int(input(f"Digite o {j + 1} valor:"))#atribui n valores inteiros no vetor.

for l in range(len(vetor_3)): #laço pra percorrer o vetor.
    vetor_3[l] = vetor[l] + vetor_2[l] #soma os dados do vetor + vetor_2 e armazena no vetor_3.
print("\n") #quebra delinha

print(f"Dados do vetor:    {vetor}") #imprime os dados que estão entre aspas e os dados da variavel vetor na tela.
print(f"Dados do vetor_2:  {vetor_2}") #imprime os dados que estão entre aspas e os dados da variavel vetor_2 na tela.
print(f"soma entre v e v_1 {vetor_3}") #imprime os dados que estão entre aspas e os dados da variavel vetor_3 na tela.






