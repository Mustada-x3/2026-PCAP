/*
Problema 1004 BeeCrowd
22.09.2026
Alice Ribeiro Marenda
LIAC - LIAC - Ler dois valores inteiros, armazenando-os em variaveis e multiplicando ambos no final, exibindo o resultado assim "PROD = resultado"
*/

#include <stdio.h>

int main(){
    int num1 = 0;
    int num2 = 0;

    scanf("%d", &num1);
    scanf("%d", &num2);

    int num3 = num1 * num2;
    
    printf("PROD = %d\n", num3);
    return 0;
}