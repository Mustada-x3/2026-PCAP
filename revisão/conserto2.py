'''
Codigo a consertar:

idade = int(input("Sua idade:"))
if idade = 18:
    print("Você tem exatamente 18 anos")
else:
    print("Você não tem 18 anos")
'''
# Problema: na linha "if idade = 18:" o termo "=" não se encaixa, pois o objetivo do código não é atribuir um valor.

# Correção:

idade = int(input("Sua idade:"))
if idade == 18:
    print("Você tem exatamente 18 anos")
else:
    print("Você não tem 18 anos")