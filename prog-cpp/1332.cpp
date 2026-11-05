/*
* Disciplina: 2026-PCAP
* Problema  : BeeCrowd 1332 - Um-Dois-Três
* Autor     : Alice Ribeiro Marenda
* LIAC      : Le N palavras. Cada uma é "one", "two" ou "three" com no máximo uma letra trocada. Mostra 1, 2 ou 3 para cada palavra.
*/

#include <iostream>
#include <string>
using namespace std;

int main() {
    int n, i;
    string s;

    cin >> n;
    for (i = 0; i < n; i++) {
        cin >> s;
        if (s.size() == 5) {
            cout << 3 << endl;
        } else if ((s[0] == 'o' && s[1] == 'n') || (s[0] == 'o' && s[2] == 'e') || (s[1] == 'n' && s[2] == 'e')) {
            cout << 1 << endl;
        } else {
            cout << 2 << endl;
        }
    }

    return 0;
}