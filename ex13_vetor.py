numero_de_pessoas = int(input("Digite o numero de pessoas:"))
vetor_idade = [int] * numero_de_pessoas
vetor_altura = [float] * numero_de_pessoas

#percorre o vetor e atribui valores inteiros informados pelo usuario no vetor_idade.
for i in range(len(vetor_idade)):
    vetor_idade[i] = int(input("Informe a idade:"))

#atribui a posição 0 vetor_idade na variavel m_velho e m_novo.
m_velho = vetor_idade[0]
m_novo = vetor_idade[0]

#laço pra percorrer o vetor, condicões para verficar o maior e o menor numero no vetor.
for i in range(len(vetor_idade)):
    if vetor_idade[i] > m_velho:
        m_velho = vetor_idade[i]
    elif vetor_idade[i] < m_novo:
        m_novo = vetor_idade[i]

#imprime os dados das variaveis e mostra na tela.
print("Dados do vetor idade:",vetor_idade)
print(f"O mais velho tem {m_velho} anos.")
print(f"O mais novo tem {m_novo} anos.")

print("\n") # quebra de linha.

#percorre o vetor e atribui valores inteiros informados pelo usuario no vetor_altura.
for i in range(len(vetor_altura)):
    vetor_altura[i] = float(input("Informe a altura:"))

#atribui a posição 0 vetor_altura na variavel m_alto e m_baixo.
m_alto = vetor_altura[0]
m_baixo = vetor_altura[0]

#laço pra percorrer o vetor, condicões para verficar o maior e o menor numero no vetor.
for i in range(len(vetor_altura)):
    if vetor_altura[i] > m_alto:
        m_alto = vetor_altura[i]
    elif vetor_idade[i] < m_baixo:
        m_baixo = vetor_altura[i]

#imprime os dados das variaveis e mostra na tela.
print("Dados do vetor altura:",vetor_altura)
print(f"O mais alto tem {m_alto} de altura.")
print(f"O mais baixo tem {m_baixo} de altura.")


