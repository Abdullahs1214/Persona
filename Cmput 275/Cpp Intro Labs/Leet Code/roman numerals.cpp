#include <iostream>

using namespace std;


int main() {
    string s = "";
    cin >> s;
    


char one = 'I', five = 'V', ten = 'X', fifty = 'L', hundred = 'C', fivehund = 'D', onethou = 'M';
        int size = s.size();
    
        int sum = 0;
        for (int i = size - 1; i >= 0; i--){
            
            char cha = s[i];
            if (s[i] == 'I' && s[i+1] == 'V'){
                cha = 'A';
            
            } if (s[i] == 'I' && s[i+1] == 'X'){
                cha = 'B';
            
            } if(s[i] == 'X' && s[i+1] == 'L'){
                cha = 'E';
            
            } if (s[i] == 'X' && s[i+1] == 'C'){
                cha = 'F';
            
            } if (s[i] == 'C' && s[i+1] == 'D'){
                cha = 'G';
            
            } if (s[i] == 'C' && s[i+1] == 'M'){
                cha = 'H';
            
            }
            switch (cha){
                case 'I':
                    sum += 1;
                    break;
                case 'A': 
                    sum -= 1;
                    break;
                case 'V':
                    sum += 5;
                    break;
                case 'B':
                    sum -= 1;
                    break;
                case 'X':
                    sum += 10;
                    break;
                case 'E':
                    sum -= 10;
                    break;
                case 'L':
                    sum += 50;
                    break;
                case 'F':
                    sum -= 10;
                    break;
                case 'C':
                    sum += 100;
                    break;
                case 'G':
                    sum -= 100;
                    break;
                case 'D':
                    sum += 500;
                    break;
                case 'H':
                    sum -= 100;
                    break;
                case 'M':
                    sum += 1000;
                    break;
            }
        } cout << sum;
}