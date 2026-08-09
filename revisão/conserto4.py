'''
Codigo a consertar:

jogada = input("pedra, papel ou tesoura?")
if jogada == "pedra" or jogada == "papel" or jogada == "tesoura":
    print("Jogada válida:", jogada)
else:
    print("Jogada inválida!")
'''
# Problema: O programa interpreta palavras com letras maiusculas e minusculas como palavras diferentes, por isso quando se digita "Pedra" o código retrata essa opção como inválida

# Correção:

jogada = input("pedra, papel ou tesoura?").lower().strip()
if jogada == "pedra" or jogada == "papel" or jogada == "tesoura":
    print("Jogada válida:", jogada)
else:
    print("Jogada inválida!")