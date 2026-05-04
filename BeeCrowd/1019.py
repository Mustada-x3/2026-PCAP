'''
Problema 1019 BeeCrowd
Alice Ribeiro Marenda
09.04.26
'''
#Objetivo: determine o tempo em horas minutos e segundos, apenas numeros inteiros, com base no tempo em segundos de um acontecimento

#---Analise(LIAC)---
#Entrada: um valor inteiro
#Processamento: calcular o valor, em segundos, em horas e minutos
#Saida: exibir "quantidade de horas:quantidade de minutos:quantidade de segundos"

S = int(input())
M = int(S / 60)
S2 = int(S - M * 60)
H = int(S / 3600)
M2 = int(M - H * 60)
print(f"{H}:{M2}:{S2}")