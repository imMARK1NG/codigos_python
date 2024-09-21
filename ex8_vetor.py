vetor = [i + 1 for i in range(365)] #decalra um vetor com 365 numeros inteiros de 0 a ...365.
media = 0 #declarando a variavel media e inicializando com o valor 0.

for i in range(len(vetor)): #laço para epercorrer o vetor.
    media += (i + 1)/365 #soma todos os valores do vetor e dividir por 365.

print("A temperatura media é:", media) #imprime os dados da variavel media e mostra na tela.
print(vetor) #imprime os dados da variavel media e mostra na tela.