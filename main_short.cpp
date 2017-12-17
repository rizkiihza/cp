#include<iostream>
using namespace std;
int main()  {
  int t; cin >> t;
  for(int i=1;i<=t;i++){
    long long  n; cin >> n;
    cout << n*(n+2)*(2*n+1)/8<< endl;
  }
}

