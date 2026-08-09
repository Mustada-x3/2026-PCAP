'''
Codigo a consertar:

contador = 1
while contador <= 5:
    print("Rodada", contador)
print("Fim de jogo")
'''
# Problema: a variavel contador mantem seu valor continuamente como 1, fazendo com que a condição de "while" nunca seja descomprida.

# Correção:

contador = 1
while contador <= 5:
    print("Rodada", contador)
    contador = contador + 1
print("Fim de jogo")