# 🎮 Adivinhe o Número
​
Jogo de adivinhação feito em Python na disciplina PCAP (Aula 16).
O computador sorteia um número e você tenta descobrir dentro de um
limite de chances. Tem 3 níveis: Fácil, Médio e Impossível.
​
# ▶️ Como jogar
1. Abra o terminal na pasta do jogo.
2. Rode: python adivinhe.py
3. Escolha o nível (1, 2, 3, 4 ou 5) e tente adivinhar!
​
# 🎚️ Níveis
- Fácil ....... 1 a 10,   3 chances
- Médio ....... 1 a 100,  5 chances
- Difícil ..... 1 a 500,  10 chances
- Impossível .. 1 a 1000, 10 chances
- Aleatório ... 1 a (número entre 11 e 999), (entre 1 e 20) chances

# 🤖 Commits 
Durante o processo de criação do jogo, o mesmo passou por diversas modificações que aumentaram sua complexidade a cada 'nível'.
Essas foram:
 v1 - O coração do jogo
    Variaveis - numero_secreto e palpite
    Tipos de dados - int e str
    Entrada/saida - input e print
    Ferramenta que sorteia um número - import random, random.randint

 v2 - Acertou ou não?
    Fazer com que o jogo reaja ao palpite do jogador
    Decisão - if/elif/else. Substitui os prints da v1 em uma estrutura de decisão na qual emite uma mensagem diferente de acordo com a resposta do jogador.
    Por exemplo: 
    if palpite == numero_secreto 
    print("Acertou! O número era", numero_secreto)

 v3 - Mais de uma chance
    Proprocionalizar 3 chances de palpite para o jogador ao invés de apenas uma.
    Criamos 2 novas variaveis - acertou e chances
    Estrutura de Repetição - fazer com que a estrutura de decisão(if/elif/else) se repita até que se acerte o resultado ou até as chances acabarem.
    Nova estrutura de decição:
    if not acertou(ou seja se a variavel acertou não for verdadeira)
    print("Suas chances acabaram! O número era", numero_secreto)

 v4 - Organizando em sub-rotina
    Guardamos o codigo em uma sub-rotina nomeada de jogar, com parametros(maxim, chances) e depois devolve um resultado com o comando return(o qual é nomeado como acertou).
    Assim o jogo fica organizado dentro de uma sub-rotina, o que permite que joguemos a quantidade de vezes que desejarmos.
    Ao final criamos uma linha de codigo que executa o jogo "venceu = jogar(10, 3)"

 v5 - Três níveis de dificuldade
    Criamos três diferentes níveis de dificuldade(Fácil, Médio e Impossìvel) com um menu para escolher o qual se deseja jogar.
    Organizamos cada nível em uma lista(nome, maximo, chances) e usamos o número digitado correspondente para determinar qual das configurações utilizar. Por exemplo: 1 = nível fácil, logo se a pessoa digitar o número 1 o programa utilizará a configuração correspondente.

 v6 - Adições pessoais
    Crição de um novo nível de dificuldade, o Aleatório. Nesse nível o programa sorteia  o número maximo a ser adivinhado e a quantidade de chances do jogador, fazendo com que o jogo se torne mais imprevissivel.
    Juntamente a esse nível foi adicionado outro, o Difícil. Ele serve como uma ponte entre o Médio e o Impossivel para que o jogador tenha mais opções.
    Agora o número secreto é revelado após a "partida", para que a pessoa saiba qual era o número mesmo que tenha perdido.