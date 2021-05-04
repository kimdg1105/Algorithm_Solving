#include <iostream>
#include <stdio.h>
#include <algorithm>
using namespace std;

int main(){
    int T;
    cin >> T;
    for (int i=0;i<T;i++){
        int n;
        cin >> n;
        long long arr[101]={1,1,1,2,2,};
        for(int j=5;j<=n;j++){
            arr[j] = arr[j-5] + arr[j-1];
        }

        cout << arr[n-1] << endl;
    }
}