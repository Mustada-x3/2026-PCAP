'''
Problema 1012 BeeCrowd
Alice Ribeiro Marenda
23.04.26
'''
#Objetivo: calcular a area do triangulo, circulo, trapezio, quadrado e retangulo se baseando em três números flutuantes

#---Analise(LIAC)
#Entrada: três números flutuantes distintos com uma casa decimal após a virgula
#Processamento: calcular a area do triangulo, do circulo, do trapezio, do quadrado e do retangulo com base nos três números dflutuantes dados
#Saida: exibir todas as areas das formas geometricas com seus noms ao lado

a, b, c = input().split()
a = float(a)
b = float(b)
c = float(c)
pi = 3.14159
T = (a * c) / 2
C = pi * c**2
T2 = ((a + b)*c) / 2
Q = b**2
R = a * b
print(f"TRIANGULO: {T:.3f}")
print(f"CIRCULO: {C:.3f}")
print(f"TRAPEZIO: {T2:.3f}")
print(f"QUADRADO: {Q:.3f}")
print(f"RETANGULO: {R:.3f}")