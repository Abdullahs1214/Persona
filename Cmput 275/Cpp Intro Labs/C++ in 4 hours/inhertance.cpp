#include <iostream>
using namespace std;

class Chef {
    public:
    void makechicken(){
        cout << "chef makes chicken" << endl;
    }
    void makesalad(){
        cout << "chef makes salad" << endl;
    }
    void makespecial(){
        cout << "chef makes special dish" << endl;
    }
};

class Italianchef: public Chef {
    public:
        void makepasta(){
        cout << "chef makes pasta" << endl;
}
};

int main() {


Chef chef;
chef.makechicken();

Italianchef italianchef;
italianchef.makepasta();
return 0;

}