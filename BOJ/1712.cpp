#include <iostream>
using namespace std;

int main(){
    long a,b,c;
    long  abx, cx;
    cin >> a >> b >> c ;
    int x;
    if(b-c >=0){
        x = -1;
    }
    else{
        x = a/(c-b)+ 1;
    }

    cout << x << endl;


}