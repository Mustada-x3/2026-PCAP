'''
Codigo a consertar
def soma_jogadas(minha, da_maquina):
    total = minha + da_maquina

pontos = soma_jogadas(3, 4)
print("A soma das jogadas foi:", pontos)
'''
# Problema: Sem o codigo return o valor 'total' definido dentro da função não pode funcionar fora dela

# Correção:

def soma_jogadas(minha, da_maquina):
    total = minha + da_maquina
    return total

pontos = soma_jogadas(3, 4)
print("A soma das jogadas foi:", pontos)