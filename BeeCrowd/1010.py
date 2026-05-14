'''
Problema 1010 BeeCrowd
Alice Ribeiro Marenda
14.05.26
'''
#Objetivo: ler o valor de uma peça, seu codigo unitario e sua quantidade e calcular e fazer o mesmo processo novamente para determinar o valor a ser gasto

#---Analise(LIAC)---
#Entrada: quatro valores inteiros e dois com duas casas decimais
#Processamento: calcular o total a ser gasto com base nos números da entrada
#Saida: exibir "VALOR A PAGAR: R$" com duas casas após o ponto decimal

c, n, v = input().split()
c = int(c)
n = int(n)
v = float(v)
vp1 = n * v

c2, n2, v2 = input().split()
c2 = int(c2)
n2 = int(n2)
v2 = float(v2)
vp2 = n2 * v2

vpd = vp1 + vp2
print(f"VALOR A PAGAR: R$ {vpd:.2f}")