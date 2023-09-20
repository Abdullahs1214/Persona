#include <iostream>
using namespace std;

class Movie{
    private:
    string rating;
    public:
    string title;
    string director;
    
    Movie(string atitle, string adirector, string arating) {
        title = atitle;
        director = adirector;
        setrating(arating);
    }
    void setrating(string arating){
        if (arating == "G" || arating == "PG" || arating == "PG-13" || arating == "R" || arating == "NR"){
            rating = arating;
        } else {
            rating = "NR";
        }
    }
    string getRating() {
        return rating;
    }
};

int main() {

    Movie avengers("The avengers", "Joss Whedon", "PG-13");
    avengers.setrating("DOG");

    cout << avengers.getRating();

    return 0;

}