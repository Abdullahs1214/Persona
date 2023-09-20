#include <iostream>
#include <vector>
using namespace std;

int main() {
    char a = 'a';
    vector<string> strs = {"flower", "flow", "flight"};
    char names[] = {};
    char letter = '((strs[0])[0])';
    cout << typeid(letter).name() << " " << letter;
    for (int i = 0; i < size(strs[i]); i++){
        for (int j = 0; j < strs.size(); j++){
            //if ((strs[j])[i] == (strs[j+1])[i]){
           //     continue;
           // }else {
           //     break;
           // }
           //cout << (strs[j][i]);
        } 
    }

    return 0;
}