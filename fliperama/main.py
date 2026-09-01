#====================================
# Arquivo:    main.py
# Disciplina: 2026 - PCAP
# Aula:       20
# Autor:      Alice Ribeiro Marenda
# Data:       2026.08.04
# Conceitos:
#====================================

# Importar funções de arquivos
from telas import titulo, linha
from adivinhe import jogar_adivinhe
from modulos import ler_opcao
from ppt import jogar_ppt
from placar import salvar_placar, carregar_placar
from jogadores import menu_jogadores, salvar_jogadores, carregar_jogadores
from par_impar import jogar_parimpar, resultado 

NOMES_DOS_JOGOS = ['Adivinhe o Número', 'Pedra-Papel-Tesoura', 'Par ou Impar']
vj = carregar_placar()
jogadores = carregar_jogadores()

OPCOES = ['0', '1', '2', '3', '4']

NOME_DO_DONO = "ALICE RIBEIRO MARENDA"

def mostrar_placar():
    titulo('PLACAR')
    for i in range(3):
        print(NOMES_DOS_JOGOS[i] + ':' + str(vj[i]) + 'x')

while True:
    
    titulo('FLIPERAMA DA ' + NOME_DO_DONO)
    print('1 - Jogo Adivinhe o número')
    print('2 - Jogo Pedra - Papel - Tesoura')
    print('3 - Jogo Par ou Impar')
    print('4 - Jogadores')
    print('0 - Sair do fliperama')
    linha()
    opcao = ler_opcao('Escolha uma opção: ', OPCOES)

    if opcao == '0':
        mostrar_placar()
        salvar_placar(vj)
        salvar_jogadores(jogadores)
        print('Até a proxima!')
        break

    if opcao == '4':
        menu_jogadores(jogadores)
    else:
        indice = int(opcao) -1
        vj[indice] = vj[indice] + 1

        if opcao == '1':
            jogar_adivinhe()
        elif opcao == '2':
            jogar_ppt()
        elif opcao == '3':
            jogar_parimpar()

    input('Presione Enter para voltar ao menu...')