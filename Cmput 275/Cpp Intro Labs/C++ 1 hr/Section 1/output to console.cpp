#include <iostream>
using namespace std;

int main() {
    int sales = 95000;
    double statetax = 0.04;
    double calcstatetax = sales*statetax;
    double countytax = 0.02;
    double calccountytax = sales*countytax;
    double totaltax = calccountytax + calcstatetax;

    cout << "Your Total Sales were $" << sales << endl
         << "Your State Tax is $" << calcstatetax << endl
         << "Your County Tax is $" << calccountytax << endl
         << "Your Total Tax payed is $" << totaltax << endl;

    return 0;
}
// need total sales, state tax, county tax, total tax payed