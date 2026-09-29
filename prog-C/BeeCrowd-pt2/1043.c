/*
Problema 1043 BeeCrowd
29.09.2026
Alice Ribeiro Marenda
LIAC - Ler 3 valores inteiros (A, B, C) e verificar se formam ou não um triângulo. Caso a resposta seja positiva, se calcula o perimetro do triângulo. Em caso negativo, se calcula a área do trapézio que tem A e B como base e C como altura, mostrando a mensagem
*/

#include <stdio.h>
int main(){
    float a, b, c;
    scanf("%f %f %f", &a, &b, &c);

    if (a < b + c && b < a + c && c < a + b){
        float p = a + b + c;
        printf("Perimetro = %.1f\n", p );
    } else{
        float r = ((a + b) * c) / 2;
        printf("Area = %.1f\n", r);
    }

    return 0;
}