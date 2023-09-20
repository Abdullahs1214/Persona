#include <iostream>
using namespace std;

int main() {
    int n;
    cin >> n;
    int an = abs(n);
    cout << (an/10) % 10;
    return 0;
}