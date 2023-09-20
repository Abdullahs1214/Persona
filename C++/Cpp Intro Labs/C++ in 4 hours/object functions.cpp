#include <iostream>
using namespace std;

class Student {
    public:
        string name;
        string major;
        double gpa;
        Student(string aname, string amajor, double agpa) {
            name = aname;
            major = amajor;
            gpa = agpa;
        }
        bool hashonour(){
            if(gpa >= 3.5){
                return true; // prints 1
            }
            return false;//prints 0
        } 
};

int main() {
    Student student1("jim", "Business", 2.4);
    Student student2("Pam", "Art", 3.6);

    cout << student2.hashonour();
    return 0;
}