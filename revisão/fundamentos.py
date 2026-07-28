# 1. Variaveis e tipos de dados
# Variaveis armazenam dados enquanto o codigo é executado. Os dados armazenados podem ser, por exemplo, a idade de uma pessoa, um nome, um valor, uma operação.
# Exemplos
nome = "M" #str - está em formato de texto
idade = int(14) #int - representa número inteiro
dinheiro_disponivel = float(1.50) #float - representa número racional
dormindo = False #bool - determina se a variavel é verdadeira ou falsa (True x False)

# 2. Operadores
# Operam dentro de um código
#Exemplos
 
 # Atribuição
dinheiro = 0 # "=" atribui um valor a variavel dinheiro

 # Operações
1 + 3 # "+"(Soma) soma os valores
5 - 9 # "-"(Subtração) subtrai os valores
129 * 2 # "*"(Multiplicação) multipica os valores
516 / 2 # "/"(Divisão) divide os valores (resultado == float)
6 // 3 # "//"(Divisão Inteira) divide os valores, ignorando o resto (resultado == int)
99 % 2 # "%"(Resto) É o que sobra da divisão
6 ** 2 # "**"(Exponenciação) Multiplicação do numero por ele mesmo, o segundo número indicada qunatas vezes isso deve ser feito

 # Comparação
9 == 9 # "=="(Igual a) - representa igualdade entre os elementos
34 != 8 # "!="(Diferença) - representa a diferença entre o elementos
5 < 8 # "<"(Menor que) - demonstra que um elemento é menor do que o outro
4 > 2 # ">"(Maior que) - demonstra que um elemento é maior do que o outro
10 <= 10 # "<="(Menor ou igual que) - demonstra que um elemento é menor ou igual em relação a outro elemento
2 >= 1 # ">="(Maior ou igual que) - demonstra que um elemento é maior ou igual em relação a outro elemento

# 3. Entrada de dados
# Envio de dados para o computador
'''
Tipos de dados:
 1. str - formato de texto
 2. int - número inteiro
 3. float - número racional
 4. bool - True x False
'''
#Exemplos
input("Qual seu nome?") # Entrada em str
int(input("Qual sua idade?")) # Entrada em int
float(input("Qual é o valor deste produto?")) # Entrada em float
maioridade = True # Entrada em bool

# 4. Saida de dados
# Dados enviados pelo computador
#Exemplo
print("Eu sou maneiro 😎")
nome = "Anomalys.Drakat"
print(f"{nome}")

# 5. Estruturas de Repetição
# Fazem com que uma determinada parte do código se repita por um numero determina ou não de vezes
#Exemplos
pão = 0
while pão < 10:
    print("Compre pão!")
    p = int(input("Quantos pães comprar?"))
    pão = pão + p

for refri in range(1,6):
    print("Coquinha gelada")
    refri = refri + 1

# 6. Estrturas de Condição
# São partes do codigo que são acionadas caso certa condição seja cumprida
#Exemplo
flor = int(input("Quantas flores você deseja?"))
if flor > 100:
    print("campo de flores")
elif 50 > flor > 100:
    print("jardim")
else:
    print("buque de flores")