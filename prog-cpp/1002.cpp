/*
* Disciplina: 2026-PCAP
* Problema  : BeeCrowd 1001 - Extremamente Básico
* Autor     : Alice Ribeiro Marenda
* LIAC      : Efetua o cálculo da área, elevando o valor de raio ao quadrado e multiplicando por π.
*/

#include <iostream>
#include <iomanip>
using namespace std;

int main() {
    double r, area;

    cin >> r;
    area = 3.14159 * r * r;
    cout << fixed << setprecision(4);
    cout << "A=" << area << endl;

    return 0;
}