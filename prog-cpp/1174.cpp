/*
* Disciplina: 2026-PCAP
* Problema  : BeeCrowd 1174 - Seleção em Vetor I
* Autor     : Alice Ribeiro Marenda
* LIAC      : Le um vetor A[100]. No final, mostra todas as posições do vetor que armazenam um valor menor ou igual a 10 e o valor armaenad0 em cada uma das posições
*/

#include <iostream>
#include <iomanip>
#include <vector>
using namespace std;

int main() {
    vector<double> a;
    double x;
    int i, qtd;

    for (i = 0; i < 100; i++) {
        cin >> x;
        a.push_back(x);
    }
    qtd = a.size();
    cout << fixed << setprecision(1);
    for (i = 0; i < qtd; i++) {
        if (a[i] <= 10) {
            cout << "A[" << i << "] = " << a[i] << endl;
        }
    }

    return 0;
}