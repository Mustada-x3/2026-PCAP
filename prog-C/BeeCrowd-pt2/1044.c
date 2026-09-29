/*
Problema 1044 BeeCrowd
29.09.2026
Alice Ribeiro Marenda
LIAC - Ler dois valores inteiros e determinar se eles são multiplos, imprindo a resposta "Sao Multiplos", para quando forem multiplos, e "Nao sao Multiplos" para quando não forem multiplos
*/

#include <stdio.h>

int main(){

    int a, b;
    scanf("%d %d", &a, &b);

    if (a % b == 0 || b % a == 0){
        printf("Sao Multiplos\n");
    }else{
        printf("Nao sao Multiplos\n");
    };

    return 0;
}