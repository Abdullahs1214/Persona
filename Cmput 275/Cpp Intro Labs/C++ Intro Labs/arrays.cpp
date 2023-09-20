#include <iostream>
using namespace std;

int main() {
    int n ;
    cin >> n;
    char word [n];
    for (int i = 0; i < n; i ++) {
    cin >> word [ i ];
    }
    for (int i = 0; i <= n ; i ++) {
    cout << word [ i ];
    }
    cout << endl ;

    }