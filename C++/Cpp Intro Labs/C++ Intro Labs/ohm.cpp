#include <iostream>
using namespace std;

bool hashrand(int n){
 int sum = 0, m = 0, N = 0;
 N = n;
 while (0 < N){    
  m = N % 10;    
  sum = sum + m;    
  N = N / 10;    
 }
 if (!(n%sum)){
  return 1;
 } else {
  return 0;
 }
}

int main() {
 int k = 0;
 cout << "Enter a Number: \n";
 cin >> k;
 while (!(hashrand(k))){
  k++;
 }
 cout << k << "\n";
}