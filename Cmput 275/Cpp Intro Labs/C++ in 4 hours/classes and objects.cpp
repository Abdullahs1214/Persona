#include <iostream>
using namespace std;

class Book {
    public: // specify attributes
        string title;
        string author;
        int pages;

};

int main() {
    
    Book book1;
    book1.title = "Demon king";
    book1.author = "Me";
    book1.pages = 500;

    Book book2;
    book2.title = "Maze runner";
    book2.author = "I";
    book2.pages = 400;
    book2.title = "Kys";

    cout << book2.title;

    return 0;
}