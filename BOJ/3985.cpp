#include <iostream>
#include <cmath>
#include <algorithm>
using namespace std;

int main(){
    int L;
    int N;
    int p,k;

    cin >> L;
    cin >> N;

    int exp[N+1]={};
    int real[N+1]={};
    int arr[L+1]={};
    int expans=0, realans = 0;
    int eidx,ridx;

    for(int i=1;i<=N;i++){
        cin >> p;
        cin >> k;
        exp[i] = k-p+1;
        for(;p<=k;p++){
            if(arr[p]==0){
                arr[p] = i;
                real[i] ++;
            }
        }
    }

    for(int i=1;i<=N;i++){
        if(expans<exp[i]){
            eidx = i;
            expans = exp[i];
        }
        if(realans<real[i]){
            ridx = i;
            realans = real[i];
        }
    }

    printf("%d\n%d",eidx, ridx);

}