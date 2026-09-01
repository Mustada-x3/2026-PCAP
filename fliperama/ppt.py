#====================================
# Arquivo:    ppt.py
# Disciplina: 2026 - PCAP
# Aula:       20
# Autor:      Alice Ribeiro Marenda
# Data:       2026.08.04
# Conceitos:
#====================================

from random import randint
from telas import titulo, linha
from modulos import ler_opcao

# 0 - PEDRA| 1 - PAPEL| 2 - TESOURA
Jogadas = ['PEDRA', 'PAPEL', 'TESOURA']

def quem_vence(jogador, computador):
    # Devolve 'empate', 'jogaodor' ou 'computador'
    if jogador == computador:
        return 'empate'
    if jogador == (computador + 1) % 3:
        return 'jogador'
    return 'computador'

def mostrar_jogadas():
    print('[0] Pedra')
    print('[1] Papel')
    print('[2] Tesoura')
    linha()

def jogar_ppt():
    titulo('PEDRA-PAPEL-TESOURA')

    pj = 0
    pc = 0

    while pj < 2 and pc < 2:
        mostrar_jogadas()

        jogador = int(ler_opcao('Sua jogada', ['0', '1', '2']))
        computador = randint(0, 2)

        print('Você jogou ' + Jogadas[jogador] + '.')
        print('O PC jogou ' + Jogadas[computador] + '.')

        resultado = quem_vence(jogador, computador)

        if resultado == 'empate':
            print('Empate! Ninguem pontua.')
        elif resultado == 'jogador':
            pj = pj +1
            print('Você venceu a rodada!')
        else:
            pc = pc + 1
            print('O PC venceu a rodada!')

        print('Placar: você ' + str(pj) +
              'x' + str(pc) + ' PC')

    if pj > pc:
        titulo('Você venceu a partida!')
    else:
        titulo('O PC venceu a partida!')