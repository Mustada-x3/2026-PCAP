'''
Problema 1008 BeeCrowd
Alice Ribeiro Marenda
09.04.26
'''
#Objetivo: criar um programa que recebe o numero de um funcionario, as horas trabalhadas e o dinheiro recebido por hora, e que calcule o salario recebido de acordo com  o numero de horas trabalhadas

#---Analise(LIAC)---
#Entrada: 2 numeros inteiros e 1 numero com 2 casas decimais, que serão respectivamente o numero do funcionario, o valor recebido por hora e a quantidade de horas trabalhadas
#Processamento: calcular o total que o funcionario ira receber de acordo com suas horas trabalhadas
#Saida: exbir "NUMBER = numero do funcionario" e "SALARY = salario do vendedor"

N = int(input())
VH = int(input())
HT = float(input())
S = HT * VH
print(f"NUMBER = {N}")
print(f"SALARY = U$ {S:.2f}") 