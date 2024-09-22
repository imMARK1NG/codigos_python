#Questão 14

tamanho = 10 #define o tamanho do vetor

#declarando um vetor com n valores inteiros.
vetor_x = [i  + 1 for i in range(10)]
vetor_y = [int] * tamanho

#inveter os dados do vetor_x e os atribui ao vetor_y.
inver = vetor_x[::-1]
vetor_y = inver

#imprime os dados da variaveis e mostra na tela.
print("Dados do vetor x:",vetor_x)
print("Dados do vetor y:", inver)

#recebe um posição do vetor.
pos = vetor_y[int(input("Digite a posição do vetor y(0 a 9):"))]

#imprime os dados da variavel e mostra na tela.
print(pos)