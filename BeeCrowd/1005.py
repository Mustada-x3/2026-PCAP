'''
Problema 1005 BeeCrowd
Alice Ribeiro Marenda
07.04.26
'''
#Objetivo: calcular a média entre A e B sendo que A tem 3.5 de peso e B tem 7.5

#---Análise(LIAC)---
#Entrada: dois valores com 1 casa decimal para cada um
#Processamento: multiplicar A e B por seus respectivos pesos, depois somar ambos e dividi-los pela soma de seus pesos
#Saída: exibir "MEDIA = media de A e B" com 5 casas decimais

A = float(input())
B = float(input())
MEDIA = ((A * 3.5) + (B * 7.5)) / (3.5 + 7.5)
print(f"MEDIA = {MEDIA:.5f}")