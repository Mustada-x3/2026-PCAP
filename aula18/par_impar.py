# =================================================================
# Disciplina : Pensamento Computacional, Algoritimos e Programação
# Projeto    : Jogo "Par ou Impar"
# Arquivo    : par_impar.py
# Autor      : Alice Ribeiro Marenda
# Data       : 25.06.26
#==================================================================

import random

def resultado(oj, r):
    if oj == r:
        return "Ganhou"
    if oj != r:
        return "Perdeu"
    
pj = 0
pm = 0


dedos = [0, 1, 2, 3, 4, 5]
opcoes = ["par", "impar"]

rodada = 1

while pj < 3 and pm < 3 and rodada < 5:
    
    print("---Rodada", rodada, "---")
    maquina = random.randint(0,5)
    
    oj = input("Par ou Impar?").lower().strip()
    jogador = int(input("Escolha um número de 0 a 5:"))

    if jogador not in dedos or oj not in opcoes:
        print("Inválido ❌")
    else:
        jogadorv = jogador

    soma = maquina + jogadorv

    if soma % 2 == 0 :
        print("Par")
        r = ("par")
    else:
        print("Impar")
        r = ("impar")
    
    quem = resultado(oj, r)
    if quem == "Perdeu":
        print("Maquina ganhou a rodada", rodada)
        pm = pm + 1
    elif quem == "Ganhou":
        print("Jogador ganhou a rodada", rodada)
        pj = pj + 1

    rodada = rodada + 1
    print(f"A jogada da maquina foi: {maquina}")
    print("Placar -> Você:", pj, "| Máquina:", pm)

if pj > pm:
    print("O jogador foi o vencedor!🎉")
elif pm > pj:
    print("A maquina ganhou!☠️")