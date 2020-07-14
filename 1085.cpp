#include <iostream>
#include <cmath>
using namespace std;

int min(int a,int b){
    if(a<b){
        return a;
    }
    else{
        return b;
    }

}

int main(){
    int x,y,w,h;
    cin >> x >> y >> w >> h;
    int ans;

    int a,b,c,d;
    a= w-x;
    b= h-y;
    b = min(a,b);
    c = min(x,b);
    d= min(c,y);


    cout << d;

}