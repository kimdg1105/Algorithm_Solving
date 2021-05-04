#include <iostream>
#include <cmath>
using namespace std;



int knap(int capacity,int item,int w[],int v[]){
    int bag[item+1][capacity+1];
    for(int a=0;a<=item;a++){
        bag[a][0] =0;
    }
    for(int a=0;a<=capacity;a++){
        bag[0][a] =0;
    }
    for(int i=1;i<=item;i++){
        for(int j=1;j<=capacity;j++){
             bag[i][j] = bag[i-1][j];
            if(w[i]<=j){
                bag[i][j] = max(bag[i][j],v[i]+bag[i-1][j-w[i]]);
            }
        }
    }

    return bag[item][capacity];
}

int main(){
    int n,k;
    cin >> n >> k;
    int w[101];
    int v[101];

    for(int i=1;i<=n;i++){
        cin >> w[i] >> v[i];
    }
    cout << knap(k,n,w,v) <<endl;

}
