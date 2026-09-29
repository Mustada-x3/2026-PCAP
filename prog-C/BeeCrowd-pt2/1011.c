/*
Problema 1011 BeeCrowd
22.09.2026
Alice Ribeiro Marenda
LIAC - calcular o volume de uma esfera, imprimindo o resultado "VOLUME = resultado"
*/

#include <stdio.h>

int main(){
    double r = 0, v = 0;
    scanf("%lf", &r);
    v = (4.0 / 3) * 3.14159 * (r * r * r);
    printf("VOLUME = %.3lf\n", v);
    return 0;
}