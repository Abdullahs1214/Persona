#include <iostream>
using namespace std;

string getdayofweek(int daynum){
    string dayname;
    switch(daynum){
        case 1:
            dayname = "Monday";
            break;
        case 2:
            dayname = "Tues";
            break;
        case 3:
            dayname = "Wed";
            break;
        case 4:
            dayname = "thur";
            break;
        case 5:
            dayname = "Fri";
            break;
        case 6:
            dayname = "sat";
            break;
        case 7:
            dayname = "Sun";
            break;
        default:
            cout << "Invalid Number";
    }
    return dayname;
} 
int main() {
   cout << getdayofweek(3);
    return 0;
}