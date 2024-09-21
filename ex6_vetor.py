#Questão 

numero_de_elementos = int(input("Digite o numero de elementos:")) #atribui n valores vetor, informados pelo usuario.
vetor = [i + 1 for i in range(numero_de_elementos)]  #atribui n valores inteiros dentro do vetor.
soma = 0 #declarando a variavel soma e inicializando ela com o valor zero.

for i in range(len(vetor)): #laço para percorrer o vetor.
    soma += i + 1 #pega o indice i e soma com mais 1.

print(vetor) #imprime os dados da variavel vetor e mostra na tela.
print(soma) #imprime os dados da variavel soma e mostra na tela.