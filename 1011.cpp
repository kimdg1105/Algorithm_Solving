#include <iostream>
using namespace std;

int main(){
    int T;
    cin >> T;
    for (int i=0;i<T;i++){
        int start = 1;
        double x,y;
        int ans;
        cin >> x >> y;

        double n = y-x;
        double np;
        long s=1;
        while(1){
            np = s*s;
            s++;
            if(np > n){
                break;
            }
        }
        s--;

        if(n== (s-1)*(s-1)){
            ans = 2*(s-1) -1;
        }
        else if(n<= ((s-1)*(s-1)+(s*s))/2){
            ans = 2*s-1-1;
        }
        else{
            ans = 2*s-1;
        }
        cout << ans << endl;
    }
}