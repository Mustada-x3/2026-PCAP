# Fliperama em C++ (MeuApp v4.0)

## O que é?
O fliperama é um programa em que se pode, a partir de um menu, jogar e cadastrar diferentes jogadores

## Como compilar e rodar
- Compilar: g++ -Wall fliperama.cpp -o fliperama
- Rodar: ./fliperama

## Arquivos
- fliperama.cpp: arquivo onde está o fliperama e suas funcionalidades, tais como jogar e salvar jogadores no arquivo jogadores.csv
- jogadores.csv: guarda o registro dos jogadores cadastrados, mesmo depois de fechar o programa

## C x C++: o que mudou
| O que | No fliperama.c (linha) | No fliperama.cpp (linha) |
| ... | ... | ... |
| guardar um jogador | strcpy(apelidos[qtd], novo) (l. _) | apelidos.push_back(novo) (1. _) |
| comparar apelidos | strcmp(...) -- 0 (l. _) | == (l. _) |
| a função que cadastra | int cadastrar(..., int qtd) (l._) | void cadastrar(...&apelidos, ...) (l._) |

## Autoavaliação
| Criterio | Conceito que espero | Onde se prova (arquivo e linha) |
| ... | ... | ... |
| 1. Estrutura, compilação e Git | A | Todos os arquivos + todos os commits das aulas realizados corretamente |
| 2. Cadastro: vectors e referência | A | Linhas 87 a 112 do fliperama.cpp e arquivo jogadores.csv |
| 3. Jogo e partidas | A | Linhas 114 a 144 do fliperama.cpp |
| 4. Persistência | A | Todos os arquivos funcionando corretamente |
| 5. Documentação e comparação | B | README.md |