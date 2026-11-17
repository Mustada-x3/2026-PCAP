/*
* Disciplina : 2026 - PCAP
* Projeto    : Meu App v4.0 - O Fliperama em C++ (Aula 32)
* Autor      : Alice Ribeiro Marenda
* LIAC       : Menu com validação, cadastro de jogadores em dois vectores que crescem, um jogo que conta partidas por jogador e o cadastro salvo em arquivo na saída e relido na entrada
*/

#include <iostream>
#include <string>
using namespace std;

#define DONO "ALICE RIBEIRO MARENDA"

void linha() {
    cout << "--------------------------------------------" << endl;
}

void titulo(string texto) {
    linha();
    cout << "   " << texto << endl;
    linha();
}

int ler_numero(string mensagem, int minimo, int maximo) {
    int numero;

    cout << mensagem << ": ";
    cin >> numero;
    
    while (cin.fail() || numero < minimo || numero > maximo) {
        if (cin.fail()) {
            cin.clear();              // Destrava o cin, que parou no que não era número
            cin.ignore(1000, '\n');   // E joga o resto da linha
        }
        cout << "Opção invalida! Tente novamente: ";
        cin >> numero;
    }
    return numero;
}

void mostrar_menu() {
    linha();
    cout << "   FLIPERAMA DO " << DONO << endl;
    linha();
    cout << "[1] Adivinhe o Número" << endl;
    cout << "[2] Cadastrar jogador" << endl;
    cout << "[3] Listar jogadores" << endl;
    cout << "[0] Sair" << endl;
    linha();
}

int main() {
    int opcao;

    mostrar_menu();
    opcao = ler_numero("Sua escolha", 0, 3);
    while (opcao != 0) {
        if (opcao == 1) {
            
        } else if (opcao == 2) {

        } else {
            
        }
        mostrar_menu();
        opcao = ler_numero("Sua escolha", 0, 3);
    }
    titulo("Até a proxima!");
    return 0;
}