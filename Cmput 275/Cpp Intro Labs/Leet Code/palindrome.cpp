#include <iostream>
using namespace std;
/*
bool ispalindrome(int x){
    int temp = x;
    long lastdigit,rx;
    while (temp > 0){
        lastdigit = temp % 10;
        temp /= 10;
        rx = rx *10 + lastdigit;
        }
        if (rx == x){
            return true;
        } else{
            return false;
        } cout << rx << " " << x << endl;
    }
*/
int main() {
    int x;
    cin >> x;
    bool flag;
    int temp = x;
int lastdigit,rx;
    while (temp > 0){
        lastdigit = temp % 10;
        temp /= 10;
        rx = rx *10 + lastdigit;
        }
        if (rx == x){
            return flag = true;
        } else{
            return flag = false;
        } 
    cout << rx << " " << x << " " << flag << endl;
    return 0;
}