#include <iostream>

int main() {
    int x = 10;
    //int y = x++; // x == 11, y == 10
    int y = ++x; // y == 11, x == 11
    std::cout << y << x;
    return 0;
}
//+,-,* work as normal
// / with 2 ints returns an int, need one double to make third double and return double
// % modulus operator returns remainder of division
// increment operator, ++, post or prefix both
// decrement operator, --