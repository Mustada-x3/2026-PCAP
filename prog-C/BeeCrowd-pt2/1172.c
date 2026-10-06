/*
Problema 1172 BeeCrowd
Alice Ribeiro Marenda
06.10.2026
LIAC: Le 10 inteiroa num vetor X. Troca os valores menores ou igual a zero por 1. Imprime cada posição no formato "X[i] = valor".
*/

#include <stdio.h>

int main() {
    int x[10], i;
     for (i = 0; i < 10; i++) {
        scanf("%d", &x[i]);
         
        if (x[i] <= 0) {
            x[i] = 1;
        }
     }
     for (i = 0; i < 10; i++) {
        printf("X[%d] = %d\n", i, x[i]);
     }

     return 0;
}