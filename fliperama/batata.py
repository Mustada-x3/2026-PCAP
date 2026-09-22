from modulos import ler_opcao, ler_numero
from telas import titulo, linha
import random
#====================================
# Arquivo:    batata.py
# Disciplina: 2026 - PCAP
# Aula:       23 - o jogo autoral do meu fliperama
# Autor:      Alice Ribeiro Marenda
# Data:       2026.08.04
# Conceitos:  Reuso de modulo próprio, função sem retorno, entrada validada, contagem de partidas
#====================================

def jogar_batata():
    '''
    Aqui você deve pegar um número e esse número te dirá a quantidade de batatas que você deve comprar
    Os números escolhidos representam os dias da semana
    Cada dia tem um intervalo de quantidade de batatas diferente
    '''
    titulo('BATATA')

    print('Dias da semana:')
    print('[0] - Domingo')
    print('[1] - Segunda')
    print('[2] - Terça')
    print('[3] - Quarta')
    print('[4] - Quinta')
    print('[5] - Sexta')
    print('[6] - Dia do juizo final, ou seja, Sabádo')
    n = ler_numero('Escolha um dia da semana:', 0, 6)
    print('Você escolheu ' + str(n))
    if n == 0:
        print('Domingo')
        m = random.randint(1, 3)
        print(m, 'Batatas')
    elif n == 1:
        print('Segunda')
        m = random.randint(1, 5)
        print(m, 'Batatas')
    elif n == 2:
        print('Terça')
        m = random.randint(3, 8)
        print(m, 'Batatas')
    elif n == 3:
        print('Quarta')
        m = random.randint(3, 10)
        print(m, 'Batatas')
    elif n == 4:
        print('Quinta')
        m = random.randint(2, 9)
        print(m, 'Batatas')
    elif n == 5:
        print('Sexta')
        m = random.randint(5, 15)
        print(m, 'Batatas')
    elif n == 6:
        print('Sabado, você tem coragem!')
        m = random.randint(30, 99)
        print(m, 'Batatas')
        print('Prepare seu dinheiro')

        linha()