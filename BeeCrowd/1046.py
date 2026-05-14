'''
Problema 1046 BeeCrowd
Alice Ribeiro Marenda
14.05.26
'''
#Objetivo: determinar em horas o tempo de duração de um jogo com base em dois valores inteiros

#---Analise(LIAC)---
#Entrada: dois numeros inteiro que representam a hora de inicio e fim do jogo
#Processamento: definir quanto tempo o jogo durou
#Saida: exibir "O JOGO DUROU XX HORAS"

h1, h2 = map(int, input().split())
if h1 == h2 :
    print("O JOGO DUROU 24 HORA(S)")
elif h1 < h2 :
    h = h2 - h1
    print(f"O JOGO DUROU %d HORA(S)" %(h))
elif h1 > h2 :
    h = (24 - h1) + h2
    print(f'O JOGO DUROU %d HORA(S)' %(h))