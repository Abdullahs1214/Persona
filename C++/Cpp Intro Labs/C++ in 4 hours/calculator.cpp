#include <iostream>
using namespace std;

int main() {
    /*
    double num1 = 0, num2 = 0;
    cout << "Enter Number 1: ";
    cin >> num1;

    cout << "Enter Number 2: ";
    cin >> num2;
    
    cout << num1 + num2;
    return 0;
*/
int num1, num2, result;
char op;
cout << "Enter first number " << "Enter operator " << "Enter second number ";
cin >> num1 >> op >> num2;

if (op == '+'){
    result = num1 + num2;
} else if (op == '-'){
    result = num1 - num2;
} else if (op == '/'){
    result = num1 / num2;
} else if (op == '*'){
    result = num1 * num2;
} else {
    cout << "Invalid Operator";
}
cout << result;





}