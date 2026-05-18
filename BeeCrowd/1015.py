'''
Problema 1015 BeeCrowd
Alice Ribeiro Marenda
18.05.26
'''
#Objetivo: ler quatro valores correspondentes aos eixos x e y em dois diferentes pontos e calcular a distância entre eles

#---Analise(LIAC)---
#Entrada: duas linhas de dados com numeros flutuantes dispostos como x e y
#Processamento: utilizar os numeros da entrada na seguinte formula ((x1 - x2) + (y1 -y2)) ** 0.5
#Saida: exibir o numero decorrente da formula anterior com quatro casas decimais após a virgula

import math
x1, y1 = list(map(float,input().split()))

x2, y2 = list(map(float,input().split()))

v = math.sqrt(pow(x1 - x2,2) + pow(y1 - y2,2)) 
print(f"{v:.4f}")