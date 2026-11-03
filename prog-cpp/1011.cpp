/*
* Disciplina: 2026-PCAP
* Problema  : BeeCrowd 1001 - Extremamente Básico
* Autor     : Alice Ribeiro Marenda
* LIAC      : Faz um programa que calcula e mostra o volume de uma esfera sendo fornecido o valor de seu raio (R
*/

#include <iostream>
#include <iomanip>
using namespace std;

int main() {
    int r;
    double volume;

    cin >> r;
    volume = (4/3.0) * 3.14159 * r * r * r;
    cout << fixed << setprecision(3);
    cout << "VOLUME = " << volume << endl;

    return 0;
}