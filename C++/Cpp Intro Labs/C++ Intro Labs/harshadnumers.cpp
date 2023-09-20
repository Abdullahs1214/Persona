
#include <iostream>

using namespace std;

int main() {
    double harshad = 0;
    int i = 0;
    int number, sum = 0;
    int number1 = 0;
    int number2 = 0;
    cout << "Enter a Number: " << endl;
    cin >> number;
    number1 = number;
    while (number1 > 0) {
        sum += (number1 % 10);
        number1 /= 10;
    } 
    double ans = number % sum;
    if (ans == 0) {
        harshad = 1;
        cout << number;
    } else {
        i = number;
        while (true){
        sum = 0;
        number2 = i;
        while (number2 > 0) {
        sum += (number2 % 10);
        number2 /= 10;
        }   double ans1 = i % sum;
        if (ans1 == 0) {
        cout << i;
        break;
        } i++;
    
    }
    } 
    return 0;
}