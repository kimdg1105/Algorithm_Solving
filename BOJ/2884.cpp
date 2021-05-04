#include <iostream>

using namespace std;

int main(){
    int sh, sm;
    int ch, cm;

    cin >> sh >> sm ;
    ch = sh;
    cm = sm- 45;
    if(cm < 0){
        cm = 60 - 45 + sm;
        ch --;
    }
    if(ch < 0){
        ch = 23;
    }

    cout << ch << " " << cm <<endl;
}