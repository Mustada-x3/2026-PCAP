'''
Problema 1037 BeeCrowd
Alice Ribeiro Marenda
23.04.26
'''
#Objetivo: criar um programa que agrupa um numero em seu intervalo, caso o numero não seja compativel com nenhum dos intervalos disponiveis uma mensagem será exibida dizendo 'fora do intervalo'

#---Analise(LIAC)---
#Entrada: um numero flutuante qualquer
#Processamento: definir a qual intervalo o numero se encontra
#Saida: exibir "Intervalo ..." ou "Fora do intervalo"

n = float(input())
if 0 <= n <= 25:
    print('Intervalo [0,25]')
if 25 < n <= 50:
    print('Intervalo (25,50]')
if 50 < n < 75:
    print('Intervalo (50,75]')
if 75 < n <= 100:
    print('Intervalo (75,100]')
if n > 100 or n < 0:
    print('Fora de intervalo')