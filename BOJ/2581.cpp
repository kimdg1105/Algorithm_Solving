#include <iostream>
#include <cmath>
using namespace std;

int main(){
    int M,N;

    cin >> M >> N;
    int len;
    len = N-M+1;
    int arr[len+1];
    int temp=M;
    int total=0;
    int mi = 10001;
    for(int i=0;i<len;i++,temp++){
        arr[i] = temp;
    }
    int ans[len+1];
    int cnt=0;
    for(int i=0;i<len;i++){
        if(arr[i]==2){
            total += arr[i];
            mi = min(mi,2);
            cnt++;

        }
        else{
        for(int j=2;j<arr[i];j++){
            if(arr[i]%j==0){
                break;
            }
            else if(j==arr[i]-1){
                total += arr[i];
                mi = min(mi,arr[i]);
            cnt ++;
            }

        }
        }

    }
    if(cnt==0){
        cout << -1;
    }
    else{
            cout << total<<endl << mi<< endl;
    }

}