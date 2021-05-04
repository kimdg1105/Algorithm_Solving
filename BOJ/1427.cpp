#include <iostream>
#include <algorithm>
using namespace std;

int main(){
    char arr;
    int n;
    cin >> n;
    int t=0;



    while(n!=0){
        arr[t] = n%10;
        n = n/10;
        t++;
    }

    for(int i=0;i<t;i++){
        cout <<arr[i] << " ";
    }

}