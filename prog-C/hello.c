/*Comentário de bloco
Programa: Hello.c
Data:     22.09.2026
Autor:    Alice Ribeiro Marenda
*/

// Importa biblioteca padrão de entrada e saída
#include <stdio.h>

// Defino a função principal do tipo int
int main(){
    // printf == Saída --> Mostra na tela 
    // "entre aspas == texto" 
    // comando encerra com ;
    printf("Hello World!\n");

    // Receber 2 valores, somar e mostrar o resultado
    int num1 = 0;
    int num2 = 0;

    printf("Digite um valor: ");
    scanf("%d", &num1);
    printf("Digite outro valor: ");
    scanf("%d", &num2);

    int soma = num1 + num2;
    printf("Soma: %d\n", soma);

    // Indica que chegou ao fim da função == retornando 0
    return 0;
}

/*
Para compilar ==
gcc <nome-do-arquivo> -o nome-do-programa

Para executar ==
./nome-do-programa
*/