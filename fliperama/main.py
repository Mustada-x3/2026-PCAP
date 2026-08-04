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

NOME_DO_DONO = "Alice.M"
OPCOES = ['0', '1']

while True:
    titulo('Fliperama da ' + NOME_DO_DONO)
    print('1 - Jogo Adivinhe o número')
    print('0 - Sair do fliperama')
    linha()
    opcao = ler_opcao('Escolha uma opção: ', OPCOES)

    if opcao == '0':
        print('Até a proxima!')
        break
    elif opcao == '1':
        jogar_adivinhe()