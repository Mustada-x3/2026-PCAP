/*
Problema 1175 BeeCrowd
Alice Ribeiro Marenda
06.10.2026
LIAC: Le 20 números inteiros num vetor N. Mostra o vetor com a ordem invertida, o último lido aparece na posição 0, o primeiro lido ma posição 19.
*/

#include <stdio.h>

int main() {
    int n[20], i;

    for (i = 0; i < 20; i++) {
        scanf("%d", &n[i]);
    }

    for (i = 0; i < 20; i++) {
        printf("N[%d] = %d\n", i, n[19 - i]);
    }

    return 0;
}