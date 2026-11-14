# Fliperama em C (MeuApp v3.0)

## O que é?
Um fliperama interativo, no qual se tem um menu onde é possivel jogar jogos e cadastrar jogadores. O programa cadastra jogadores e mantem seus arquivos guardados, o apelido e número de vezes jogadas, até mesmo após se encerar a atividade do programa.

## Como compilar e rodar
Compilar: gcc -Wall Fliperama.c -o Fliperama
Rodar: ./Fliperama

## Arquivos
- Fliperama.c: A raiz do fliperama, onde tudo funciona. Possui um menu onde se pode cadastrar jogadores e jogar.
- jogadores.csv: O arquivo que guarda as informações dos jogadores cadastrados,ou seja, seus apelidos e número de partidas.

## Python x C: O que mudou
| O que | No jogadores.py (linha) | No Fliperama.c (linha) |
| ... | ... | ... |
| guardar um jogador | jogadores.append(novo) (1._) | strcpy(apelidos[qtd], novo) (1._) |
| comparar apelidos | == (1._) | strcmp(...) == 0 (1._) |
| abrir sem arquivo | exists(ARQUIVO) (1._) | fopen == NULL (1._) |

## O que o C me obrigou a decidir
A forma de programação C me obrigou a aprender novas formas de realizar codigos e linhas de codigo diferentes, para que o programa funcionasse corretamente

## Autoavaliação
| Critério | Conceito que espero | Onde se Prova (arquivo) |
| ... | ... | ... |
| 1. Estrutura, compilação e Git | A ou B | Fliperama.c, commits fora do codespace |
| 2. Cadastro: menu, funções e vetores | A | jogadores.csv |
| 3. Jogo e partidas | A ou B | Fliperama.c |
| 4. Persistência| ? | ?
| 5. Documentação e comparação | B | README.md, Fliperama.c e jogadores.csv |