from os.path import exists
from telas import titulo, linha
from modulos import ler_opcao, ler_texto

ARQUIVO = 'jogadores.csv'


#======================================================================================================================================================
# Arquivo:    jogadores.py
# Disciplina: 2026 - PCAP
# Aula:       22 - MeuApp v2.0: o cadastro de jogadores
# Autor:      Alice Ribeiro Marenda
# Revisado:   Aula 23 - validação de campo vazio e documentação
# Data:       2026.08.04
# Conceitos:  Registros como lista de campos, cadastro como lista de listas, cadastrar, listar, buscar, alterar, excluir, persistencia em arquivo .csv
#======================================================================================================================================================

# O que esse arquivo é:
#  A quarta gaveta do projeto. O telas.py cuida do que aparece
#  O modulos.py cuida do que o programa pergunta, o placar.py
#  Cuida de quantas partidas cada jogo teve, e o jogadores.py
#  Cuida de quem jogou

# O registro:
#  Cada jogador é uma lista de três campos, sempre nesta ordem:
#    indice 0 -> apelido | 1 -> nome | 2-> partidas
#  É o cadastro e uma lista dessas listas

def cadastrar(jogadores):
    '''
    Pergunta o apelido e nome, e acrescenta um jogador ao cadstro
    
    Não devolve nada: o cadastro muda no lugar
    '''

    titulo('NOVO JOGADOR')

    apelido = ler_texto('Apelido (sem espaços)').lower()
    nome = ler_texto('Nome completo')

    novo = [apelido, nome, '0']
    jogadores.append(novo)

    print('Jogador' + apelido + ' cadastrado')
    linha()

def listar(jogadores):
    titulo('JOGADORES CADASTRADOS')

    if len(jogadores) == 0:
        print('Nenhum jogador cadastrado ainda')
    else:
        for jogador in jogadores:
            print(jogador[0] + ' | ' + jogador[1] + ' | ' + jogador[2] + ' partidas')

    linha()

def buscar(jogadores, apelido):
    '''
    Procura um apelido no cadastro e diz onde ele está
    
    Parametros:
        jogadores (list) - o cadastro inteiro
        apelido   (str)  - o apelido procurado, em minusculas
        
    Retorno:
        int - a posição do jogador na lista, ou -1 se não achar
    '''
    
    for i in range(len(jogadores)):
        if jogadores[i][0] == apelido:
            return i

    return -1

def alterar(jogadores):
    listar(jogadores)

    apelido = ler_texto('Apelido de quem vai mudar de nome: ').lower()
    i = buscar(jogadores, apelido)

    if i == -1:
        print('Não achei ninguem com esse apelido')
    else:
        print('Nome atual: ' + jogadores[i][1])
        jogadores[i][1] = ler_texto('Nome novo')
        print('Pronto. Agora seu nome é ' + jogadores[i][1])

    linha()

def excluir(jogadores):
    '''
    Procura um apelido no cadastro e exclui a ficha do jogador da memória permanentemente
    Antes de excluir a ficha do jogador, o programa, pergunta se deve prosseguir, caso a resposta seja positiva ele realiza a ação
    '''

    listar(jogadores)

    apelido = input('Apelido de quem vai sair do cadstro: ').strip().lower()
    i = buscar(jogadores, apelido)

    if i == -1:
        print('Não achei ninguem com esse apelido')
    else:
        print('Vou apagar o cadastro de ' + jogadores[i][1])
        print('[1] Confirmar')
        print('[2] Deixar com está')
        certeza = ler_opcao('Sua escolha', ['1', '2'])

        if certeza == '1':
            jogadores.pop(i)
            print('Cadastro apagado')
        else:
            ('Nada foi apagado')

    linha()

def salvar_jogadores(jogadores):
    arquivo = open(ARQUIVO, 'w')

    for jogador in jogadores:
        arquivo.write(jogador[0] + ', ' + jogador[1] + ', ' + jogador[2] + '\n')

    arquivo.close()

def carregar_jogadores():
    if not exists(ARQUIVO):
        return []

    arquivo = open(ARQUIVO, 'r')
    linhas = arquivo.readlines()
    arquivo.close()

    lidos = []
    for linha_lida in linhas:
        campos = linha_lida.strip().split(',')
        lidos.append(campos)

    return lidos

def menu_jogadores(jogadores):
    carregar_jogadores()
    while True:
        titulo('CADASTRO DE JOGADORES')
        print('[1] Cadastrar jogador')
        print('[2] Listar jogadores')
        print('[3] Alterar nome')
        print('[4] Excluir jogador')
        print('[0] Voltar ao fliperama')
        linha()

        opcao = ler_opcao('Sua escolha' , ['0', '1', '2', '3', '4'])

        if opcao == '0':
            break
        elif opcao == '1':
            cadastrar(jogadores)
        elif opcao == '2':
            listar(jogadores)
        elif opcao == '3':
            alterar(jogadores)
        else:
            excluir(jogadores)