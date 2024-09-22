#Questão 12

tamanho = int(input("Digite o tamanho do vetor:")) #atribui uma valor n do tipo inteiro na variavel tamanho.

#declarando um vetor com n valores inteiros.
vetor = [int] * tamanho 
vetor_2 = [int] * tamanho 
vetor_3 = [int] * tamanho

for i in range(len(vetor)): #laço para percorrer o vetor.
    vetor[i] = int(input(f"Digite o {i + 1} valor:")) #atribui valores inteiros informados pelo usuario no vetor. 

for j in range(len(vetor)): #laço para percorrer o vetor.
    vetor_2[j] = vetor[j] + vetor[j]  #faz a soma dos dados do primeiro vetor com ele mesmo e adiciona em um novo vetor.

for l in range(len(vetor)): #laço para percorrer o vetor.
    vetor_3[l] = vetor[l] * vetor[l] #faz a mult dos dados do primeiro vetor com ele mesmo e adiciona em um novo vetor.

#imprime os dados das variaveis e mostra na tela.
print("Dados do vetor:")
print("",vetor)
print("",vetor)

print("A soma é igual a:\n", vetor_2)
print("A mult é igual a:\n",vetor_3)
