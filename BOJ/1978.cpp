#include <iostream>
using namespace std;

int main(){
    int n;
    cin >> n;
    int arr[n+1];
    for(int i=0;i<n;i++){
        cin >> arr[i];
    }
    int ans[n];
    int cnt=0;
    for(int i=0;i<n;i++){
        if(arr[i]==2){
                cnt++;
        }
        else{
        for(int j=2;j<arr[i];j++){
            if(arr[i]%j==0){
                break;
            }
            else if(j==arr[i]-1){
                
            cnt ++;
            }

        }
        }

    }
    cout << cnt << endl;
}