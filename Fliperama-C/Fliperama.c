/*
* Disciplina: 2026-PCAP
* Projeto   : Fliperama em C
* Autor     : Alice Ribeiro Marenda
* LIAC      : 
*/

#include <stdio.h>
#define DONO "Alice Ribeiro Marenda"

void linha() {
    printf("¨¨¨¨¨¨¨¨¨¨¨¨¨¨¨¨¨¨¨¨¨¨¨¨¨¨¨¨¨¨¨¨¨¨¨¨¨¨¨¨¨¨¨\n");
}

void titulo(char texto[]) {
        linha();
        printf("    %s\n", texto);
        linha();
    }

int ler_numero(char mensagem[], int minimo, int maximo) {
    int numero, lidos;

    printf("    %s: ", mensagem);
    lidos = scanf("%d", &numero);
    while (lidos != 1 || numero < minimo || numero > maximo) {
        if (lidos != 1) {
            scanf("%*s");  // Joga fora o que não era número
        }
        printf("Opção inválida! Tente novamente: ");
        lidos = scanf("%d", &numero);
    }
    return numero;
}

void mostrar_menu() {
    linha();
    printf("    FLIPERAMA DO %s\n", DONO);
    linha();
    printf("[1] Adivinhe o Número\n");
    printf("[2] Cadastrar jogador\n");
    printf("[3] Listar jogadores\n");
    printf("[0] Sair");
    linha();
}

int main() {
    int opcao;

    mostrar_menu();
    opcao = ler_numero("Sua escolha", 0, 3);
    while (opcao != 0) {
        if (opcao == 1) {
            // O jogo entra na Fase 3
        }else if (opcao == 2) {
            // O cadastro entra na Fase 2
        } else {
            // A lista entra na Fase 2
        }
        mostrar_menu();
        opcao = ler_numero("Sua escolha", 0, 3);
    }
    titulo("    Até a proxima!");
    return 0;
}