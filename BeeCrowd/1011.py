'''
Problema 1011 BeeCrowd
Alice Ribeiro Marenda
07.04.26
'''
#Objetivo: ler o raio de uma esfera e calcular seu volume com a formula (4/3) * pi * R**3

#---Análise(LIAC)---
#Entrada: um valor de ponto flutuante(raio R)
#Processamento: aplicação da formula do volume da esfera
#Saída: exibir "VOLUME = valor da formula" com três casas decimais

R = float(input())
pi = 3.14159
V = (4.0 / 3.0) * pi * R**3
print(f"VOLUME = {V:.3f}")