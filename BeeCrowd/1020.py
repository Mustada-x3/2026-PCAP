'''
Problema 1020 BeeCrowd
Alice Ribeiro Marenda
09.04.26
'''
#Objetivo: determinar um numero inteiro, idade em dias, e determinar a idade de uma pessoa

#---Analise(LIAC)---
#Entrada: um numero inteiro
#Processamento: calcular a idade de uma pessoa com base no numero em dias dado
#Saida: exibir "ano(s) mes(es) dia(s)"

D = int(input())
A = D // 365
D = D % 365
M = D // 30 
D = D % 30
print(f"{A} ano(s)")
print(f"{M} mes(es)")
print(f"{D} dia(s)")