'''
Problema 1014 BeeCrwd
Alice Ribeiro Marenda
16.04.26
'''
#Objetivo: determinar os km percorridos por litro de gasolina de um automovel com base em seus km percorridos e a gasolina gasta

#---Analise(LIAC)---
#Entrada: um numero inteiro r um real com uma casa após a virgula
#Processamento: calcular a relação entre a quantidade de km percorridos e o total de gasolina gasto
#Saida: demonstrar "consumo do automovel km/l" com três casas após a virgula
 
km = int(input())
l = float(input())
kl = km/l
print(f"{kl:.3f} km/l")