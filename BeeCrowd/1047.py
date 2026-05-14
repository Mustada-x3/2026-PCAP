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

h1, m1, h2, m2 = input().split()
h1 = int(h1)
m1 = int(m1)
h2 = int(h2)
m2 = int(m2)

if (h1 == 1) and (m1 < m2):
    r1 = 60 - m1
    m = r1 -m2
    h = 0
    print("O JOGO DUROU %d HORA(S) E %d MINUTOS(S)" %(h, m))
elif (h1 < h2) and (m1 < m2):
    h = h2 - h1
    m = m2 - m1
    print("O JOGO DUROU %d HORA(S) E %d MINUTO(S)" %(h, m))
elif (h1 == h2) and (m1 == m2):
    print("O JOGO DUROU 24 HORA(S) E 0 MINUTO(S)")
elif (h1 < h2) and (m1 > m2):
    h = (h2 - h1)-1
    r1 = 60 - m1
    m = r1 + m2
    print("O JOGO DUROU %d HORA(S) E %d MINUTO(S)" %(h. m ))
elif (h1 == h2) and (m1 < m2):
    m = m2 - m1
    print("O JOGO DUROU 0 HORA(S) E %m MINUTO(S)")
elif (h1 > h2):
    h=(24 - h1) + h2
    m= m2 - m1
    if (m1 > m2):
        h = h-1
        m = (6 - m1) + m2
        print("O JOGO DUROU %d HORA(S) E %d MINUTO(S)" %(h,m))
    else:
        print("O JOGO DUROU %d HORA(S) E %d MINUTO(S)" %(h,m))