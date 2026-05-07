'''
Problema 1044 BeeCrowd
Alice Ribeiro Marenda
16.06.26
'''
#Objetivo: verificar se dois numeros inteiros são multiplos entre si

#---Analise(LIAC)---
#Entrada: dois numeros inteiros
#Processamento: identificar maior e menor, verificar se maior % menor == 0
#Saida: "Sao Multiplos" e "Nao sao Multiplos"

A, B = input().split()
A = int(A)
B = int(B)
if A > B:
    maior = A
    menor = B
else:
    maior = B 
    menor = A
if maior % menor == 0:
    print("Sao Multiplos")
else:
    print("Nao sao Multiplos")