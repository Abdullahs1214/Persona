#include <iostream>
using namespace std;

int main() {
    int t = 0, n = 0;
    cin >> t;
    for (int i = 0; i < t; i++){
    cin >> n;
    int ans = 1;
    for (int p = 1; p <= n; p++){
    ans *= p;
    
    if (p == n){
    cout << ans % 10 << endl;
    }
    }
    } 
    return 0;
}
