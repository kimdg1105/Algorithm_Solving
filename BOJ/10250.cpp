#include <iostream>
#include <malloc.h>
using namespace std;

int main(){
    int t;
    cin >> t;
    for(int i=0;i<t;i++){
        int h,w,n;
        int rh,rw;
        cin >> h >> w >> n;
        if(h>=n){
            rh =n;
            rw = 1;
        }
        else{
            if(h == 1){
                rh = 1;
                rw = n/h;
            }
            else{
                if(n%h==0){
                    rh = h;
                    rw = n/h;
                }
                else{
                    rh = n%h;
                                rw = n/h+1;

                }

            }

        }

        if(rw<10){
            cout << rh << "0" << rw <<endl;

        }
        else{
            cout << rh << rw << endl;
        }

    }

}