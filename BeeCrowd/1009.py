'''
Problema 1009 BeeCrowd
Alice Ribeiro Marenda
07.04.26
'''
#Objetivo: calcular o total que o vendedor irá receber com base em seu salário e a comissão de vendas

#---Análise(LIAC)---
#Entrada: nome do vendedor e dois valores de dupla precissão com duas casas decimais
#Processamento: calculo que une o salário do vendedor a sua comissão, que 15% do valor de suas vendas
#Saída: apresentar "TOTAL = ganho total do vendedor" 

N = input()
V1 = float(input())
V2 = float(input())
T = V1 + (V2 * 0.15)
print(f"TOTAL = R$ {T:.2f}")