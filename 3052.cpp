#include <iostream>
using namespace std;

int main(){
    int num[1000] = {};
    int arr[10];
    int cnt =0;

    for(int i=0;i<10;i++){
        cin >> arr[i];
    }

    for(int i=0;i<10;i++){
        int k;
        k = arr[i]%42;
        for(int j=0;j<1000;j++){
            if(k == j){
                num[j] ++;
            }

        }
    }

    for(int r=0;r<1000;r++){
        if(num[r] > 0){
            cnt ++;
        }
    }
    cout << cnt << endl;
}
