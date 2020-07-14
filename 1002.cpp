#include <iostream>
#include <cmath>
using namespace std;

int main(){
    int x1,x2,y1,y2,r1,r2;
    int t;
    cin >> t;
    for(int i=0;i<t;i++){
        cin >> x1 >> y1 >> r1 >> x2 >> y2>> r2;
        double len=0;
        len = sqrt((x2-x1)*(x2-x1) + (y2-y1)*(y2-y1));
        int pick=0;
        pick = max(r1,r2);
        pick = max(pick,int(len));
        if(x1==x2 && y1== y2 && r1==r2){
            cout << -1 << endl;
        }
        else{
            if(pick ==r1 || pick ==r2){
                cout << 0 << endl;
            }
            else{
                if(r1+r2 > pick){
                    cout << 2 << endl;
                }
                else if(r1+r2==pick){
                    cout << 1 << endl;
                }
            }

        }

    }
}