#include <iostream>
using namespace std;

int main() {
    cout << "Enter 3 integers: ";
    int x;
    double y;
    int z;
    cin >> x >> y >> z;
    double ans = (x+y+z)/3;
    cout << ans;
    return 0;
}