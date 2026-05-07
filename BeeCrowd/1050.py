'''
Problema 1050 BeeCrowd
Alice Ribeiro Marenda
07.05.26
'''
#Objetivo: ler um numero inteiro que representa um codigo de DDD, em seguida informando a qual cidade pertence, caso o DDD não esteja na lista a mensagem "DDD não cadrastado"

#---Analise(LIAC)---
#Entrada: um numero inteiro correspondete ao DDD
#Processamento: definir a cidade a qual o DDD pertence
#Saida: cidade do DDD inserido, caso o DDD não esteja listado o programa informará "DDD não listado"

N = int(input())
if N == 61 :
    print("Brasilia")

if N == 71 :
    print("Salvador")

if N == 11 :
     print("Sao Paulo")

if N == 21 :
     print("Rio de Janeiro")

if N == 32 :
     print("Juiz de Fora")

if N == 19 :
    print("Campinas")

if N == 27 :
    print("Vitoria")

if N == 31 :
    print("Belo Horizonte")
if N != 61 or 71 or 11 or 21 or 32 or 19 or 27 or 31 :
    print("DDD nao cadastrdo")                    