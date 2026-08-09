'''
Codigo a consertar:
jogos = ["Adivinhe o Número", "Pedra-Papel-Tesoura", "Par ou Ímpar"]
opcao = int(input("Escolha seu jogo (1, 2 ou 3):"))
print("Você escolheu:", jogos[opcao])]
'''
# Problema: O programa de Python começa a contar a partir de 0, por isso ao digitar 3 o jogo quebra, pois não existe uma opção 3 para o computador

# Correção:

jogos = ["Adivinhe o Número", "Pedra-Papel-Tesoura", "Par ou Ímpar"]
opcao = int(input("Escolha seu jogo (1, 2 ou 3):"))
print("Você escolheu:", jogos[opcao - 1])