#include <iostream>
using namespace std;

int main() {
    int a = 1;
    int b = 2;
    int temp = a;
    a = b;
    b = temp;
    cout << a << b;
    return 0;
}

// second solution
//#include <iostream>
//using namespace std;

//int main() {
//    int a = 1;
//    int b = 2;
//    swap(a,b);
//    
 //  
//    cout << a << b;
//    return 0;
//}