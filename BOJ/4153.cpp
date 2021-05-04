#include <iostream>
#include <cmath>
using namespace std;

int main(){
    int a,b,c;
    while (1){
        cin >> a >> b >> c;
        if(a==0 && b== 0 && c==0){
            break;
        }
        else{
                    int maxi;
        maxi = max(a,b);
        maxi = max(maxi,c);
        int r1,r2,r3;
        r1 = a*a + b*b;
        r2 = a*a + c*c;
        r3 = b*b + c*c;
        if(maxi*maxi == r1 ||maxi*maxi == r2 || maxi*maxi ==r3 ){
            cout << "right" << endl;
        }
        else{
            cout << "wrong" << endl;
        }

        }
    }

}