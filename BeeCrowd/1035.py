'''
Problema 1035 BeeCrowd
Alice Ribeiro Marenda
14.05.26
'''
#Objetivo: ler 4 valores inteiros(A, B, C, D), se B for maior que C e D for maior que A , a soma de C e D for maior do que a de A e B, sendo C e D positivos e A um numero par exibir "Valores aceitos", caso o contrario exibir "Valores nao aceitos"

#---Analise(LIAC)---
# Entrada: quatro valores inteiros
# Processamento: determinar se B > C, D > A, D + C > A + B, D e C sendo numeros positivos e A é par
# Saida: caso a analise seja correta exibir "Valores aceitos", caso o contrário exibir "Valores nao aceitos"

A, B, C, D = input().split()
A = int(A)
B = int(B)
C = int(C)
D = int(D)
if (((B > C) and (D > A)) and ((A + B) < (D + C)) and ((C > 0) and (D > 0)) and (A % 2 == 0)) :
    print("Valores aceitos")
else: 
    print("Valores nao aceitos")