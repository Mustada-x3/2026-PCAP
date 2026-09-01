from modulos import ler_opcao

batatas = ['Cozida', 'Frita', 'Purê', 'Assada', 'Sopa']
def mostrar_batatas():
    print('[0] - Batata cozida')
    print('[1] - Batata Frita')
    print('[2] - Purê de batata')
    print('[3] - Batata assada')
    print('[4] - Sopa de batata')

def jogar_batata():
    print('É uma bela tarde, vamos cozinhar batatas')

    print('Podemos fazer as seguintes receitas:')
    mostrar_batatas
    r = ler_opcao('Qual receita vamos fazer?', batatas)
    