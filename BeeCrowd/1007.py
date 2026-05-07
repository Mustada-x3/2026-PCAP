'''
Problema 1007 BeeCrowd
Alice Ribeiro Marenda
16.04.26
'''
#Objetivo: ler quatro inteiros e caucular a diferença, ou seja, =(A * B) - (C * D)

#---Analise(LIAC)---
#Entrada: quatro valores inteiros, A, B, C e D
#Processamento: calcular a diferença entre A*B e C*D
#Saida: "DIFERENÇA = valor da diferença" com valores inteiros

A = int(input())
B = int(input())
C = int(input())
D = int(input())
dif = (A * B) - (C * D)
print(f"DIFERENCA = {dif}")