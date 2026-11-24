/*
* Disciplina : 2026-PCAP
* Projeto    : MeuApp v5.0 - o Fliperama em Java (Aula 33)
* Autor      : Alice Ribeiro Marenda
* LIAC       : Menu do Fliperama em java> metodos que desenham, um que le um número dentro de uma faixa, e o laçõ que s[ó para no 0
*/

import java.util.Scanner;

public class Fliperama {
    static final String DONO = "ALICE";
    static Scanner teclado = new Scanner(System.in);

    static void linha() {
        System.out.println("---------------------------------");
    }

    static void titulo(String texto) {
        linha();
        System.out.println("    " + texto);
        linha();
    }

    static int lerInteiro(){
        int numero = -1;

        if (teclado.hasNextInt()) {
            numero = teclado.nextInt();
        }
        teclado.nextLine();
        return numero;
    }

    static int lerNumero(String mensagem, int minimo, int maximo) {
        int numero;

        System.out.print(mensagem + ": ");
        numero = lerInteiro();
        while (numero < minimo || numero > maximo) {
            System.out.print("Opção invalida! Tente de novo: ");
            numero = lerInteiro();
        }
        return numero;
    }

    static void mostrarMenu() {
        linha();
        System.out.println("    FLIPERAMA DO " + DONO);
        linha();
        System.out.println("[1] Adivinhe o Número");
        System.out.println("[2] Cadastrar jogador");
        System.out.println("[3] Listar jogadores");
        System.out.println("[0] Sair");
        linha();
    }

    public static void main(String[] args) {
        int opcao;

        mostrarMenu();
        opcao = lerNumero("Sua escolha", 0, 3);
        while (opcao != 0) {
            if (opcao == 1) {

            } else if (opcao == 2) {

            } else {

            }
            mostrarMenu();
            opcao = lerNumero("Sua escolha", 0, 3);
        }

        titulo("Até a proxima!");
    }
}