# ======================================================================
# Diciplina : Pensamento Computacional. Algoritimos e Programação (PCAP)
# Projeto   : Jogo "Adivinhe o Número"
# Arquivo   : adivinhe.py
# Autor     : Alice Ribeiro Marenda
# Data      : 28.05.26
#=======================================================================

import random

def jogar(maximo, chances):
    numero_secreto = random.randint(1, maximo)
    acertou = False

    while chances > 0 and not acertou:
        palpite = int(input("Seu palpite (1 a " + str(maximo) + ")"))

        if palpite == numero_secreto:
            print("🎉 Acertou! O número era", numero_secreto)
            acertou = True
        elif palpite < numero_secreto:
            print("🔽 Muito baixo! Tente um número maior.")
        else:
            print("🔼 Muito alto! Tente um número menor.")

        chances = chances - 1 
        print("Chances restantes:", chances)
        
    print("O número secreto era:", numero_secreto)

    return acertou

c2 = random.randint(1, 20)
n = random.randint(1, 999)

niveis = [
    ["Fácil", 10, 3],
    ["Médio", 100, 5],
    ["Difícil", 500, 10],
    ["Impossível", 1000, 10],
    ["Aleatório",n, c2],
]

print("Escolha o nível de dificuldade:")
print("1 - Fácil        (1 a 10, 3 chances")
print("2 - Médio        (1 a 100, 5 chances)")
print("3 - Difícil      (1 a 500, 10 chances)")
print("4 - Impossível   (1 a 1000, 10 chances)")
print("5 - Aleatório    (1 a 999, de 1 a 20 chances)")
opçao = int(input("Digite 1, 2, 3, ou 5: "))

nivel = niveis[opçao - 1]

print("Você escolheu o nível:", nivel[0])
venceu = jogar(nivel[1], nivel[2])

if not venceu:
    print("💀 Fim de jogo! Tente um nível mais fácil. 😎")
