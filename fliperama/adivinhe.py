#====================================
# Arquivo:    adivinhe.py
# Disciplina: 2026 - PCAP
# Aula:       20
# Autor:      Alice Ribeiro Marenda
# Data:       2026.08.04
# Conceitos:
#====================================

# Importar bibliotecas e funções
from random import randint
from telas import titulo, linha
from modulos import ler_numero

def jogar_adivinhe():
    titulo('Jogo Adivinhe o Numero')
    print('Tente adivinhar o numero que estou pensando entre 1 e 10')
    segredo = randint(1, 10)
    tentativas = 0
    acertou = False

    while not acertou:
        palpite = ler_numero('Digite seu palpite', 1, 10)
        tentativas += 1

        if palpite < segredo:
            print('O numero secreto é maior. Tente novamente')
        elif palpite > segredo:
            print('O numero secreto é menor. Tente novamente')
        else:
            acertou = True

    else:        
        linha()
        print(f'Parabéns! Você acertou o numero secreto {segredo} em {tentativas} tentativas')
        linha()