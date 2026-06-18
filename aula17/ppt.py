# ======================================================================
# Disciplina : Pensamento Computacional, Algoritmos e Programação (PCAP)
# Projeto    : Jogo "Pedra - Papel - Tesoura"
# Arquivo    : ppt.py
# Autor      : Alice Ribeiro Marenda
# Data       : 16.06.26
# ======================================================================

import random

def resultado(jogador, maquina):
    if jogador == maquina:
        return "empate"
    if jogador == "pedra" and (maquina == "tesoura" or maquina == "lagarto"):
        return "jogador"
    if jogador == "papel" and (maquina == "pedra" or maquina == "spock"):
        return "jogador"
    if jogador == "tesoura" and (maquina == "papel" or maquina == "lagarto"):
        return "jogador"
    if jogador == "lagarto" and (maquina == "papel" or maquina == "spock"):
        return "jogador"
    if jogador == "spock" and (maquina == "tesoura" or maquina == "pedra"):
        return "jogador"
    return "maquina"

opçoes = ["pedra", "papel", "tesoura", "lagarto", "spock"]

pontos_jogador = 0
pontos_maquina = 0

for rodada in range(1, 6):
    print("--- Rodada", rodada, "---")

    jogada_maquina = random.choice(opçoes)
    jogada_jogador = input("Sua jogada(pedra, papel, tesoura, lagarto ou spock):").lower().strip()

    if jogada_jogador not in opçoes:
         print("❌ Invalida! Você perde a rodada!")
         pontos_maquina = pontos_maquina + 1
    else:
        quem = resultado(jogada_jogador, jogada_maquina)
        if quem == "empate":
            print("🤝 Empate!")
        elif quem == "jogador":
            print("🎉 Você ganhou a rodada!")
            pontos_jogador = pontos_jogador + 1
        else:
            print("💀 A maquina ganhou a rodada!")
            pontos_maquina = pontos_maquina + 1
    print ("A máquina jogou:", jogada_maquina)
    
print("Placar final -> Você:", pontos_jogador, ", Máquina:", pontos_maquina)
if pontos_jogador > pontos_maquina:
    print("🎇Você ganhou o jogo!")
elif pontos_maquina == pontos_jogador:
    print("🤝 Vocês empataram, não há vencedor!")
else:
    print("💀 A máquina ganhou, mais sorte na próxima vez!")