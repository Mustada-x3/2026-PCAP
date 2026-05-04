'''
Problema 1018 BeeCrowd
Alice Ribeiro Marenda
30.04.26
'''
#Objetivo: ler um valor inteiro, calcular no menor numero de notas possiveis no qual o valor pode ser decomposto. Mostrando o valor lido e a relação de notas necessárias

#---Analise(LIAC)---
#Entrada: um valor inteiro N
#Processamento: separar o valor inteiro em valores(notas) de 100 a 1 
#Saida: lista da notas e sua quantidade

n = int(input())
m = n

n100 = n // 100; n = n % 100
n50 = n // 50; n = n % 50
n20 = n // 20; n = n % 20
n10 = n // 10; n = n % 10
n5 = n // 5; n = n % 5
n2 = n // 2; n = n % 2
n1 = n 

print(f"{m}")
print(f'{n100} nota(s) de R$ 100,00')
print(f'{n50} nota(s) de R$ 50,00')
print(f'{n20} nota(s) de R$ 20,00')
print(f'{n10} nota(s) de R$ 10,00')
print(f'{n5} nota(s) de R$ 5,00')
print(f'{n2} nota(s) de R$ 2,00')
print(f"{n1} nota(s) de R$ 1,00")