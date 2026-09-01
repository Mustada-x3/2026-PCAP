import random
from modulos import ler_opcao
from telas import linha

def resultado(oj, r):
    if oj == r:
        return 'v'
    if oj != r:
        return 'd'
    return 'r'


def jogar_parimpar():
    
    pj = 0
    pm = 0

    opcoes = ['impar', 'par']
    d_m1 = [0, 1, 2, 3, 4, 5]

    while pm < 3 and pj < 3:

        oj = input('Par ou Impar?').lower().strip()
        dedosj = ler_opcao("Escolha um numero de 0 a 5:", ['0', '1', '2', '3', '4', '5'])
        dedosn = int(dedosj)

        dedosm = random.randint(0, 5)
        
        s = dedosn + dedosm

        if s % 2 == 0:
            print('Par')
            r = 'par'
        else:
            print('Impar')
            r = 'impar'

        q = resultado(oj, r)
        
        if q == 'd':
            print("Maquina ganhou a rodada")
            pm = pm + 1
        elif q == 'v':
            print("Jogador ganhou a rodada")
            pj = pj + 1
        
        print('A maquina jogou:', dedosm)
        print('Voce jogou:', dedosn)
        print('Pontos Jogador:', pj)
        print('Pontos Maquina:', pm)

    if pm < pj:
        print('Vitoria definitiva: Jogador!')
    else:
        print('Vitoria definitiva: Maquina!')