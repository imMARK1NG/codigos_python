#Questão 3

tamanho = int(input("Digite o tamanho do  vetor:")) #atribui um valor n para a variavel tamanho.
vetor = [int] * tamanho #declarando um vetor de numeros inteiros, * tamanho multiplica a quantidade de valores que teram dentro do vetor.

soma = 0 #declarando a variavel soma e a inicializando com o valor zero.
for i in range(len(vetor)): #laço para percorrer o vetor.
    vetor[i] = int(input(f"Digite o {i + 1} valor:")) #atribui valores n valores inteiros no vetor.

print("\n") #quebra de linha

print("Dados do vetor:") #imprime ps dadps entre aspas e mostra na tela.
for i in range(len(vetor)): #laço para pervorrer o vetor.
    print(vetor[i], end=" ") #imprime os dados do vetor[i] e mostra na tela.

print("\n") #quebra de linha

pos1 = int(input("Digite a primeira posição:")) #recebe um valor n para definir a posição do vetor que vai ser atribuido na variavel pos1.
pos2 = int(input("Digite a segunda posição:")) #recebe um valor n para definir a posição do vetor que vai ser atribuido na variavel pos2.

x = vetor[pos1] #atribui o valor do variavel pos1 na variavel x.
y = vetor[pos2] #atribui o valor da variavel pos2 na variavel y

soma = x + y #soma entre a variavel x e y.

print("primeiro numero selecionado:",x) #imprime os dados entre aspas e os dados da variavel x.
print("segundo numero selecionado:",y) #imprime os dados entre aspas e os dados da variavel y.
print("a soma é igual a:",soma) #imprime os dados entre aspas e os dados da variavel soma.

