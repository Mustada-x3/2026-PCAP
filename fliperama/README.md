# Fliperama da Alice Ribeiro Marenda

Um fliperama de terminal com quatro jogos, placar que não esquece e cadastro de jogadores.
Projeto da disciplina PCAP, 1° ano do Técnico em Informática do IFPR

## O que ele faz

- Quatro jogos pelo menu: Adivinhe o Número, Pedra-Papel-Tesoura, Par ou Impár e Batatas
- Placar que conta quantas vezes cada jogo foi jogado e continua contando depois de fechar o programa
- Cadastro de jogadores: cadastrar, listar, alterar e excluir

## Como rodar

```
cd fliperama
python3 main.py
```

## Os arquivos

- `main.py`      - o gabinete: menu, placar e chamadas
- `telas.py`     - ferramentas visuais
- `modulos.py`   - ferramentas de lógica: as três funções que perguntam e conferem
- `placar.py`    - quantas partidas cada jogo teve
- `jogadores.py` - quem são os jogadores
- `adivinhe.py`, `ppt.py`, `par_impar.py`, `batata.py` - um arquivo por jogo
- `placar.csv` e `jogadores.csv` - os dados, que nascem sozinhos

A função `ler_texto` ficou no `modulos.py` porque ela é utilizada para verificar se o que foi escrito está dentro do correto, essa função é uma ferramenta lógica como as outras em seu arquivo

## De onde ele veio

- Aula 20: os jogos viraram um programa só, com módulos e menu
- Aula 21: entrou o Pedra-Papel-Tesoura e o placar passou a sobreviver
- Aula 22: entrou o cadastro de jogadores, com as quatro operações
- Aula 23: campo em branco barrado e o projeto documentado

## O que ainda não funciona

- Nome com vírgula quebra a linha do arquivo, porque a vírgula é o separador.
- Os apelidos não podem possuir espaços e são escritos apenas com letras minusculas.
- Os jogos são mais limitados que suas versões originais de outras aulas, pois para colocá-los no fliperama seu código foi simplificado e funções distintas, como diferentes dificuldades no Adivinhe, ficaram para trás.