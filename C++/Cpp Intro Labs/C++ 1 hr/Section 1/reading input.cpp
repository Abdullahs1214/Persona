#include <iostream>
using namespace std;

int main() {
    cout << "Enter degree in Farenheit: ";
    int tempf;
    double tempcelsius = (tempf -32) * (5/9);

    cin >> tempf;
    cout << tempcelsius;

    return 0;
}