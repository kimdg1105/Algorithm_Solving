#include <iostream>
#include <vector>
using namespace std;


int main(){
    int n;
    cin >> n;
    int m=0;

    for(int i=0;i<n;i++){
        int num;
        vector <int> arr;
        num = i;
        int cnt = 0;
        while (num>0){
            arr[cnt] = num%10;
            num = num/10;
            cnt++;
        }

        // m += i;
        // for(int j=0;j<i;j++){
        //     m += arr[j];
        // }
        // if(m == n){
        //     break;
        //     cout << i << endl;
        // }
        // else{
        //     m=0;
        // }
         for(int j=0;j<cnt;j++){
        cout << arr[j] << " ";
    }
    }

    if(m==0){
        cout << 0 << endl;
    }
}