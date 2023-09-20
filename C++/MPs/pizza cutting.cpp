#include <iostream>
#include <cmath>
using namespace std;

int main(){
	// declare your variables
	int n, m, i = 0;
	int o = 0;
	cin >> n >> m;

	while (i <= 20) {
		if (pow(n,i) == m) {
		o = 1;
		break;
		}i++;
	} 
    if (o == 1){
        cout << "GOOD" << endl;
        } else {
        cout << "BAD" << endl;
	}// read the input

	// solve, good luck!

	return 0;
}
