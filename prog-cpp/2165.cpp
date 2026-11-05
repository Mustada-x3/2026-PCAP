/*
* Disciplina: 2026-PCAP
* Problema  : BeeCrowd 2165 - Twitting
* Autor     : Alice Ribeiro Marenda
* LIAC      : Le um linha de texto (pode ter espaço). Se tiver até 140 caracteres imprime "TWEET", se tiver mais, "MUTE"
*/

#include <iostream>
#include <string>
using namespace std;

int main() {
    string texto;

    getline(cin, texto);
    if (texto.size() <= 140) {
        cout << "TWEET" << endl;
    } else {
        cout << "MUTE" << endl;
    }

    return 0;
}