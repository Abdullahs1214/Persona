#include <iostream>
#include <cstdlib>
#include <ctime>
using namespace std;

int main() {
    const short minvalue = 1;
    const short maxvalue = 6;
    srand(time(0));
    short die1 = (rand() % (maxvalue -minvalue +1)) + minvalue;
    short die2 = (rand() % (maxvalue -minvalue +1)) + minvalue;
    cout << die1 << ", " << die2;
    return 0;

}