#include <iostream>
#include <cmath>
#include <array>
using namespace std;



void tos(long int* arr){
    // int len = (sizeof(arr)/sizeof(int));
    for(int i=2;i<=250000;i++){
        if(arr[i]==0){
            continue;
        }
        for(int j=i+i;j<=250000;j+=i){
            arr[j] = 0;
        }
    }
}

int count(long int arr[], int n){
    int cnt = 0;
    for(int i=n+1;i<=2*n;i++){
        if(arr[i]!=0){
            cnt ++;
        }
    }
    return cnt;

}

int main(){
    int n;
    long int arr[250000]={};

    for(int i=2;i<=250000;i++){
        arr[i] = i;
    }
    tos(arr);

    while (1){
        cin >> n;
        if(n ==0){
            break;
        }
        else{
            cout << count(arr,n) << endl;
        }
    }

}
