'''
Codigo a consertar:

print("===ADIVINHE O NUMERO===")
segredo = 7
palpite = input("Digite um número de 1 a 10")
if palpite == segredo:
    print("Acertou!")
else:
    print("Errou! O segredo era", segredo)
'''
# Problema; o palpite não é lido como número pela maquina, pois é necessário um comando como "int" para isso.

# Correção:

print("===ADIVINHE O NUMERO===")
segredo = 7
palpite = int(input("Digite um númer de 1 a 10"))
if palpite == segredo:
    print("Acertou!")
else:
    print("Errou! O segredo era", segredo)