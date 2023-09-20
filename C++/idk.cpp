#include <iostream>
#include <cmath>
using namespace std;

bool isPrime(int n){
    if (n <= 1){
        return false;
    }
    for (int i = 2; i <= sqrt(n); i++){
        if(n % i == 0){
            return false;
        }
    }
    return true;
};
void twinPrimes(int k){
    int check1, check2;
    for (int i = 0; i <= 1000; i++){
        bool check1 = isPrime(i);
        bool check2 = isPrime(i+2);
        if(check1 && check2){
            
        }
    }
}


int main(){
    char select;
    string prime;
    int n,k;
    cin >> select;
    if (select == 'p'){
        cin >> n;
        cout << isPrime(n);
    }else if (select == 't'){
        cin >> k;
    }

}