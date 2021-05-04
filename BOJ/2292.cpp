#include <iostream>
using namespace std;

int main(){
    int start = 1;
    long n;

    cin >> n;
    int mult = 6;
    int stb=1, endb=1;
    int i=1;
    while(n>stb){
            stb = endb+1;
            endb = endb+mult*i;
            i++;
            if(n<=endb){
                break;
            }


    }

    cout << i << endl;

}