'''
Problema 1047 BeeCrowd
Alice Ribeiro Marenda
14.05.26
'''
#Objetivo: determinar o tempo de jogo com a informação de quando o jogo começou e quando ele terminou

#---Analise(LIAC)---
#Entrada: quatro numeros inteiros que representam as horas e minutos do jogo
#Processamento: determinar por meio de uma operação matematica quanto tempo o jogo durou
#Saida: exibir "O JOGO DUROU XX HORAS E XX MINUTOS"

h1, m1, h2, m2 = map(int,input().split())
tim = (h1 * 60) + m1
tfm = (h2 * 60) + m2

if tim > tfm:
    ttm = (tfm - tim) + (24 * 60)
else:
    ttm = tfm - tim

if ttm == 0 :
    ttm = 24 * 60
print(f"O JOGO DUROU {ttm // 60} HORA(S) E {ttm % 60} MINUTO(S)")