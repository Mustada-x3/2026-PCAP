'''
Problema 1013 BeeCrowd
Alice Ribeiro Marenda
14.05.26
'''
#Objetivo: ler tres valores e determinar por meio de uma formula qual é o maior 

#---Analise(LIAC)---
#Entrada: tres valores inteiros
#Processamento: calcular qual o maior numero entre os que foram apresentados na entrada
#Saida: exibir "XX eh o maior"

a, b, c = input().split()
a = int(a)
b = int(b)
c = int(c)

m1 = (a + b + abs(a - b)) / 2
m2 = (m1 + c + abs(m1 - c)) / 2
print(f"{m2:.0f} eh o maior")