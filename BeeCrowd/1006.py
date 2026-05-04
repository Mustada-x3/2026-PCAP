'''
Problema 1006 BeeCrowd
Alice Ribeiro Marenda 
09.04.26
'''
#Objetivo: calcular a media de notas de um aluno com 3 notas de pesos diferentes

#---Analise(LIAC)---
#Entrada: 3 valores com 1 casa decimal cada um
#Processamento: calculo das medias com base nas notas obtidas e no peso de cada uma
#Saida: exibir a mensagem "MEDIA = valor da media" 

N1 = float(input())
N2 = float(input())
N3 = float(input())
M = float(((N1 * 2) + (N2 * 3) + (N3 * 5)) / (2 + 3 + 5))
print(f"MEDIA = {M:.1f}")