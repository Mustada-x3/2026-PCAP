'''
Problema 1035 BeeCrowd
Alice Ribeiro Marenda
14.05.26
'''
#Objetivo: ler 4 valores inteiros(A, B, C, D), se B for maior que C e D for maior que A , a soma de C e D for maior do que a de A e B, sendo C e D positivos e A um numero par exibir "Valores aceitos", caso o contrario exibir "Valores nao aceitos"

#---Analise(LIAC)---
'''
Problema 1038 BeeCrowd
Alice Ribeiro Marenda
14.05.26
'''
#Objetivo: ler o codigo de um item de uma tabela de lanches e sua quantidade, em seguda calcular o total a ser gasto de acordo com a quantidade e o produto

#---Analise(LIAC)---
#Entrada: dois valores inteiros, um sendo o codigo do item e o outro a quantidade
#Processamento: calcular o preço com base nos numeros de entrada
#Saida: exibir "Total: R$" com duas casas após o ponto decimal

c = int(input())
q = int(input())
if c == 1 :
    n1 = 4.00 * q
    print(f"Total: R$ {n1:.2f}")
elif c == 2 :
    n2 = 4.50 * q
    print(f"Total: R$ {n2:.2f}")
elif c == 3 :
    n3 = 5.00 * q
    print(f"Total R$ {n3:.2f}")
elif c == 4 :
    n4 = 2.00 * q 
    print(f"Total: R$ {n4:.2f}")
elif c == 5 :
    n5 = 1.50 * q
    print(f"Total: R$ {n5:.2f}")