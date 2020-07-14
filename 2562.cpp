#include <iostream>
using namespace std;

int main(){
    int arr[10];
    for(int i=0;i<9;i++){
        cin >> arr[i];
    }
    int max =0;
    int flag=0;
    for(int i=0;i<9;i++){
        if(max <= arr[i]){
            max = arr[i];
            flag = i+1;
        }
    }
    cout << max << endl;
    cout << flag << endl;
}