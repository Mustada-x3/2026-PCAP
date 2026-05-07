'''
Problema 1017 BeeCrowd
Alice Rbeiro Marenda
23.04.26
'''
#Objetivo: calcular a quantidade de gasolina um automovel que faz 12 km/l gastou durante uma viagem

#---Analise(LIAC)---
#Entrada: dois números inteiros, o tempo de viagem(em horas) e a velocidade média(em km/h)
#Processamento: calcular a quantidade de km percoridos e determinar a quantidade de gasolina gasta
#Saida: A quantidade de litros que será utilizada na viagem com três casas decimais após a virgula

h = int(input())
vm = int(input())
g = (h * vm) / 12
print(f"{g:.3f}")