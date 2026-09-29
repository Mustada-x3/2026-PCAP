/*
Problema 1002 BeeCrowd
22.09.2026
Alice Ribeiro Marenda
LIAC - Calcular a área do circulo com base no tamanho do raio dele
*/

#include <stdio.h>

int main(){
    double r = 0, a = 0;
    scanf("%lf", &r);
    a = 3.14159 * (r * r);
    printf("A=%.4lf\n", a);
    return 0;
}