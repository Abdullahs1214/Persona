#include <iostream>
using namespace std;
/*
functions:
void sayhi(string name, int age);

int main() {
    sayhi("cortana", 19);
    sayhi("covenant", 1000);
    sayhi("spade", 65);
    return 0;

}
void sayhi (string name, int age){
    cout << "Hello " << name << ", you are " << age << " years old" << endl;

} 
*/
// return statements


double cube(double num) {
    double result = num * num * num;
    return result;
}

int main() {
    double answer = cube(5.0);
    cout << answer;
    return 0;
}