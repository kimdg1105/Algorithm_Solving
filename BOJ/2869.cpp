#include <iostream>
using namespace std;

int main(){
    long up,down,day,goal;
    cin >> up >> down >> goal;
    day = (goal-down)/(up-down);
    if((goal-down)%(up-down)!=0){
        day++;
    }
    cout << day <<endl;
}