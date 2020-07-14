#include <iostream>
using namespace std;

int main(){
    int n;
    int real;
    cin >> n;
    int layer =0;
    int i=1;
    int up, down;
    real = n;
    while (n>0){
        n = n-i;
        i++;
        layer++;
    }

    int b=0;
    for(int j=1;j<layer;j++){
        b += j;
    }

    real = real -b;

    if(layer %2==0){
        up = 1;
        down = layer;
    }
    else{
        up = layer;
        down = 1;
    }
    for(int k=1;k<real;k++){
        if(layer%2==0){
            up++;
            down--;
        }
        else{
            up--;
            down++;
        }
    }

    cout << up<<"/"<< down << endl;

}