/*
* Disciplina: 2026-PCAP
* Problema  : BeeCrowd 1001 - Extremamente Básico
* Autor     : Alice Ribeiro Marenda
* LIAC      : Le 3 palavras que definem o tipo de animal possível. Em seguida conclue qual dos animais que está disponivel em uma gama de aniamais foi escolhido, através das três palavras fornecidas
*/

#include <iostream>
#include <string>
using namespace std;

int main() {
    string a, b, c;

    cin >> a >> b >> c;

    if(a == "vertebrado") {
        if (b == "ave") {
            if (c == "carnivoro") {
                cout << "aguia" << endl;
            } else {
             cout << "pomba" << endl;
            }
        } else {
            if (c == "onivoro") {
                cout << "homem" << endl;
            } else {
                cout << "vaca" << endl;
            }
         }
    } else {
        if (b == "inseto") {
            if (c == "hematofago") {
                cout << "pulga" << endl;
            } else {
                cout << "lagarta" << endl;
            }
        }else {
            if (c == "hematofago") {
                cout << "sanguessuga" << endl;
            } else {
                cout << "minhoca" << endl;
            }
        }
    }

    return 0;
}