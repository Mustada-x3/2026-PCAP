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
elif N == 71 :
    print("Salvador")
elif N == 11 :
     print("Sao Paulo")
elif N == 21 :
     print("Rio de Janeiro")
elif N == 32 :
     print("Juiz de Fora")
elif N == 19 :
    print("Campinas")
elif N == 27 :
    print("Vitoria")   
elif N == 31 :
    print("Belo Horizonte")        
else:
    print("DDD nao cadastrado")