/*
Problema 1165 BeeCrowd
Alice Ribeiro Marenda
08.10.2026
LIAC: Le N casos. Para cada inteiro X, diz se X eh primo ou não no formato "X eh primo" / "X nao eh primo".
*/

#include <stdio.h>

int eh_primo(int n) {
    int i;

    if (n <2) {
        return 0;
    }
    for (i = 2; i * i <= n; i++) {
        if (n % i == 0)
        return 0;
    }
    return 1;
}

int main() {
    int casos, k, x;

    scanf("%d", &casos);

    for (k = 0; k < casos; k++) {
        scanf("%d", &x);
        if (eh_primo(x)) {
            printf("%d eh primo\n", x);
        }else {
            printf("%d nao eh primo\n", x);
        }
    }

    return 0;
}