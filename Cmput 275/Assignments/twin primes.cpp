#include <iostream>
#include <cmath>
using namespace std;

bool isPrime(int n){
    if (n <= 1){
        return false;
    }
    int a = n / n;
    int b = n / 1;
    if (a == 1 && b == n){
        return true;
    }else {
        return false;
    }
};


int main(){
    cin >> n;
    isPrime(n);
}