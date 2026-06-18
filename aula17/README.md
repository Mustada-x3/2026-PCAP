# ✊✋✌️ Pedra-Papel-Tesoura
​
Jogo de Pedra-Papel-Tesoura feito em Python na disciplina PCAP (Aula 17).
Você joga contra o computador em uma melhor de 5 rodadas, com placar.
​
## ▶️ Como jogar
1. Abra o terminal na pasta do jogo.
2. Rode: python ppt.py
3. A cada rodada, digite pedra, papel ou tesoura.
4. Ao fim das 5 rodadas, o programa mostra o placar final.
​
## ⚙️ Como funciona (resumo)
A cada rodada o computador sorteia uma jogada (random.choice) e lê a sua.
O texto digitado é limpo (.lower().strip()) e validado (in) antes de comparar.
Uma sub-rotina decide quem venceu e o programa soma os pontos das 5 rodadas.
​
## 🧠 O que eu pratiquei
- Strings e métodos de texto: .lower() e .strip() para limpar o que foi digitado
- Validação com in: aceitar só pedra, papel ou tesoura
- Comparação de textos (==): descobrir empate e vitórias
- random.choice: sortear a jogada da máquina
- Repetição (for): jogar as 5 rodadas e manter o placar
- Sub-rotinas (def/return): isolar a regra do jogo
​
## 🎯 Autoavaliação
Conceito pretendido: [ A / B / C / D ]
​
Justificativa (cite arquivo e linha de cada critério):
- O jogo funciona ............: ppt.py, linhas 11 a 50
- Trabalho com texto .........: ppt.py, linha 35  (.lower().strip(), in, ==)
- Documentação e Git .........: este README + commits no GitHub
  * v1 - O coração do jogo
   As jogadas são textos(strings) armazenadas em uma lista.
   Utilizamos random.choice para que a maquina "escolha" uma das opções na lista.
   Em seguida se pede a jogada do jogador, a qual se deve escolher qual opção jogar.
   Ao final as jogadas de ambos são mostradas na tela do jogador, para que ele entenda quem ganhou com base em seu próprio raciocinio.
  * v2 - Tratando o texto digitado
   Aqui nos utilizamos .lower(), que deixa tudo minusculo e .strip(), o qual remove o espaço sobrando nas pontas. Tudo isso é feito porque para o computador "pedra" e "Pedra" são informações diferentes, então transformamos o que a maquina não processaria para a informação que está na lista.
   utilizamos também o operador in para verificar se a jogada está dentro das opções validas.
  * v3 - Quem ganhou?
   Fazemos com que o jogo compare as duas jogadas, utilizando if/elif/else, para determinar o que é empate, vitória do jogador e vitória da máquina.
  * v4 - Melhor de 5
   Adicionamos o sistema de rodadas com estrutura de repetição for com range.
   Além do mais existem 2 contadores de pontos que armazenam a quantidade de vitórias totais da máquina e do jogador. E ao terminar todas as 5 rodadas o computador demonstra o total de pontos de cada um.
  * v5 - Organizando em sub-rotina
   Na v4 as comparações precisavam ser muito repetitivas no laço para funcionar, por isso agora movemos a regra do jogo para dentro de uma sub-rotina chamada resultado, a qual devove um texto com return: "empate", "maquina" ou "jogador. O laço lê esse resultado e o utiliza para atualizar o placar e mandar a mensagem correta.

- Adições pessoais:
 * Pedra-Papel-Tesoura-Lagarto-Spock
 * Vitória definitiva - define quem foi o real vencedor com base na quantidade de vitórias de cada um.

AUTOR: Alice Ribeiro Marenda