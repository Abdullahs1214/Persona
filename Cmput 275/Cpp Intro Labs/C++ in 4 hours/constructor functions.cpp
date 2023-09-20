#include <iostream>
using namespace std;

class Book {
    public: // specify attributes
        string title;
        string author;
        int pages; 

        Book(){ // initial information incase no info is given
            title = "no title";
           author = "no author";
            pages = 0;
        }
        // initializng object values in construcctor
        // rather than maually defining
        Book(string atitle, string aauthor, int apages){
            title = atitle;
            pages = apages;
            author = aauthor;
        }


};

int main() {
    
    Book book1("Demon king", "Me", 500);
   

    Book book2("Maze runner","I", 400);

    Book book3;
    cout << book3.title;

    return 0;
}