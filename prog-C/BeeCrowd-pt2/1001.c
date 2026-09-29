/*
Problema 1001 BeeCrowd
22.09.2026
Alice Ribeiro Marenda
LIAC - Ler dois valores inteiros, armazenando-os em variaveis e somando ambos no final, exibindo o resultado assim "X = resultado"
*/

#include <stdio.h>

int main(){
    int num1 = 0;
    int num2 = 0;

    scanf("%d", &num1);
    scanf("%d", &num2);

    int num3 = num1 + num2;
    
    printf("X = %d\n", num3);
    return 0;
}