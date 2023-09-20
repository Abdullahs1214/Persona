#include <iostream>
using namespace std;

int main() {
    int age = 19;
    int *pAge = &age; // pointer variable
    double gpa = 2.7;
    double *pGpa = &gpa;
    string name = "Mike";
    string *pName = &name;

cout << *pAge << endl;

    return 0;
} 