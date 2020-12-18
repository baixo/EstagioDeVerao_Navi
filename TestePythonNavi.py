import math

#PRIMEIRO PROBLEMA

def conta_multiplos():
    cont = 0                                             #Cria um contador para saber a quantidade de números que seguem as restrições

    for i in range(1, 5000001):                         #Para cada "i" entre 1 e 5000001 (1 inclusivo e 5000001 exclusivo)
        if (i%2 == 0 and i%49 == 0 and i%39 ==0):       #Se o "i" tiver o resto pela divisão por 2, 39 e 49 = 0
            cont += 1                                   #Adiciona 1 no valor do contador
    return cont

print('Há '+ str(conta_multiplos()) + ' números pares e divisíveis por 39 e 49 entre 1 e 5000000.')

#------------------------------------------------------------------------------------------------#
#SEGUNDO PROBLEMA

def cria_vetor():                                       #Função que cria o vetor segundo os critérios 
    x = list(range(10))                                 #Cria um vetor com 10 indices

    for i in x:
        if i%2 == 0:                                    #Se ele for par, segue a equação
            x[i] = 3**i + 7*math.factorial(i)
        else:                                           #Se ele não for par (ímpar), segue a equação
            x[i] = 2**i + 4*math.log(i) 
    return x                                            #Retorna a o vetor

def maior_media(lista):                                 #Função que recebe um valor lista, que será o vetor criado pela função cria_vetor()
    media = round(sum(lista) / len(lista), 2)           #Arrendonda o somatório dos valores da lista e divide pelo seu tamanho (média)
    pos_maior = lista.index(max(lista))                 #Pega o index (posição) do valor máximo dentro da lista

    return media, pos_maior                             #Retorna 2 valores, a média e a posição do maior valor da lista, respectivamente

print('-----------------------------------------------------')
vetor = cria_vetor()
print('O vetor criado é:')
print(vetor)
print('A média dos valores da lista é: (com 2 casas decimais)')
print(maior_media(vetor)[0])
print('A posição do maior valor da lista é:')
print(maior_media(vetor)[1])

#------------------------------------------------------------------------------------------------#
#TERCEIRO PROBLEMA

alunos = ['Adalberto', 'Mario', 'Reginaldo', 'Creosvaldo', 'Mochileiro']            #Cria duas listas, uma com os nomes dos alunos, e uma outra com as notas
notas = [9.5, 3, 8.2, 5.8, 7.6]                                                     #dos respectivos alunos

def cria_dic(alunos, notas):                                                        #Cria função que recebe duas listas, com os nomes dos alunos e outra com as notas
    dic = {}                                                                        #Cria um dicionário vazio, que serão armazenadas as informações
    maior_nota = 0                                                                  #Cria uma variável que será armazenada a maior nota
    melhor_aluno = ''                                                               #Cria uma variável que será armazenada o melhor aluno

    for i in range(len(alunos)):                                                    #Para a quantidade de alunos (5)       
        dic[alunos[i]] = str(notas[i])                                              #Adiciona no dicionário cada aluno e sua nota correspondente
    
    for h in dic:                                                                   #Analisando então cada nota no dicionário
        if float(dic[h]) > maior_nota:                                              #Se a nota dele for maior que a maior nota até agora (inicialmente = 0)
            maior_nota = float(dic[h])                                              #Substitui a maior nota registrada
            melhor_aluno = h                                                        #E classifica ele como melhor aluno
    return melhor_aluno, maior_nota                                                 #Retorna o melhor aluno e a maior nota, respectivamente

print('-----------------------------------------------------')
print('O melhor aluno foi o', cria_dic(alunos, notas)[0], 'com', cria_dic(alunos, notas)[1] )
